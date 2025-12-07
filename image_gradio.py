import gradio as gr
import numpy as np
import scipy.signal as signal


def hello(img, do_grayscale, do_contrast, contrast, do_edges):

    luma = np.array([0.2126, 0.7152, 0.0722])

    if img is None:
        return None

    # work in float64 0..1 for stable numeric ops
    img = img.astype(np.float64) / 255.0

    if do_grayscale:
        # handle RGB/RGBA and single-channel images
        if img.ndim == 3 and img.shape[2] >= 3:
            img = img[..., :3] @ luma
        else:
            img = img @ luma

    if do_contrast:
        img = (((img - img.mean()) * contrast) + img.mean()).clip(0, 1)

    if do_edges:
        # https://stackoverflow.com/questions/53670456/intuition-behind-edge-detection-matrices-in-convolution-neural-network
        # Use two kernels (vertical and horizontal) and compute the average
        # We'll use Sobel-like kernels for better gradients
        gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
        gy_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float64)

        if img.ndim == 2:
            gx = signal.convolve2d(img, gx_kernel, mode="same", boundary="symm")
            gy = signal.convolve2d(img, gy_kernel, mode="same", boundary="symm")
            grad = (np.abs(gx) + np.abs(gy)) / 2.0
            # normalize to 0..1
            m = grad.max()
            if m > 0:
                grad = grad / m
            img = grad

        elif img.ndim == 3:
            has_alpha = img.shape[2] == 4
            rgb = img[..., :3] if img.shape[2] >= 3 else img

            gx_ch = []
            gy_ch = []
            for c in range(rgb.shape[2]):
                gx_c = signal.convolve2d(
                    rgb[:, :, c], gx_kernel, mode="same", boundary="symm"
                )
                gy_c = signal.convolve2d(
                    rgb[:, :, c], gy_kernel, mode="same", boundary="symm"
                )
                gx_ch.append(gx_c)
                gy_ch.append(gy_c)

            gx_arr = np.stack(gx_ch, axis=2)
            gy_arr = np.stack(gy_ch, axis=2)

            grad = (np.abs(gx_arr) + np.abs(gy_arr)) / 2.0

            max_val = grad.max()
            if max_val > 0:
                grad = grad / max_val

            if has_alpha:
                alpha = img[:, :, 3:4]
                img = np.concatenate([grad, alpha], axis=2)
            else:
                img = grad

        img = img.clip(0, 1)

    return img


app = gr.Interface(
    fn=hello,
    inputs=[
        gr.Image(label="Immagine da Processare", width=720, height=480),
        gr.Checkbox(label="Grayscale"),
        gr.Checkbox(label="Contrast"),
        gr.Slider(label="Contrast Factor", minimum=0.1, maximum=5.0, value=1.0),
        gr.Checkbox(),
    ],
    outputs=gr.Image(label="Risultato", width=720, height=480),
    title="Image Processing",
)

app.launch(theme=gr.themes.Citrus())
