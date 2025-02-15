import streamlit as st
from io import BytesIO
import qrcode


# Configurar o layout e título da página
st.set_page_config(page_title="QR Code", layout="centered")
st.sidebar.header("Instruções")
st.sidebar.write("""
- Gerador de QRCode
- Caso tenha alguma idéia para publicarmos, envie uma mensagem para: 11-990000425 (Willian)
- Contribua com qualquer valor para mantermos a pagina no ar. PIX (wpyagami@gmail.com)
""")



def generate_qr_code(data):
    qr = qrcode.QRCode(  # Corrigido de qrcode.Qrcode para qrcode.QRCode
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Salvar a imagem em memória
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes

st.title("Gerador de QR Code")

# Entrada de texto/link
data = st.text_input("Digite um texto ou link para gerar o QR Code:")

if data:
    img_bytes = generate_qr_code(data)
    st.image(img_bytes, caption="Seu QR Code", use_container_width=False)
    
    # Botão para baixar a imagem
    st.download_button(
        label="Baixar QR Code",
        data=img_bytes,
        file_name="qrcode.png",
        mime="image/png"
    )
