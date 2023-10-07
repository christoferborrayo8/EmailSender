import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com' 
smtp_port = 587  
smtp_username = 'ALGUN_CORREO@gmail.com'
smtp_password = 'contraseña del correo'

df = pd.read_csv('Grupos.csv') 
# Mensajes

correos_por_grupo = {}

def enviar_correo(destinatarios, asunto, mensaje, archivos_adjuntos=None):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(destinatarios)
    msg['Subject'] = asunto
    cuerpo = MIMEText(mensaje, 'html')
    msg.attach(cuerpo)

    if archivos_adjuntos:
        for archivo_adjunto in archivos_adjuntos:
            with open(archivo_adjunto, 'rb') as archivo:
                adjunto = MIMEApplication(archivo.read(), Name=archivo_adjunto)
            adjunto['Content-Disposition'] = f'attachment; filename="{archivo_adjunto}"'
            msg.attach(adjunto)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        texto_del_mensaje = msg.as_string()
        server.sendmail(smtp_username, destinatarios, texto_del_mensaje)
        print(f'Correo enviado a: {", ".join(destinatarios)}')
    except Exception as e:
        print(f'Error al enviar el correo a {", ".join(destinatarios)}: {str(e)}')
    finally:
        server.quit()

for index, row in df.iterrows():
    grupo = row['Grupo']
    carnet = row['Carnet']
    nombre = row['Nombre']
    correo = row['Correo']

    if grupo not in correos_por_grupo:
        correos_por_grupo[grupo] = {'correos': [], 'integrantes': []}

    correos_por_grupo[grupo]['integrantes'].append(f'{carnet} - {nombre}')
    if pd.notna(correo):
        correos_por_grupo[grupo]['correos'].append(correo)

# Envía los correos por grupo
for grupo, data in correos_por_grupo.items():
    mensaje = f'<strong>Grupo {grupo}</strong><br>Integrantes:<br>'
    mensaje += '<br>'.join([f'- {nombre}' for nombre in data['integrantes']])
    if grupo % 3 == 0:
        archivos_adjuntos = ['Archivo especifico 1.pdf']
    elif grupo % 3 == 1:
        archivos_adjuntos = ['Archivo especifico 2.pdf']
    else:
        archivos_adjuntos = ['Archivo especifico 3.pdf']
    archivos_adjuntos.append('Archivo general.pdf')
    enviar_correo(data['correos'], 'ASUNTO DEL CORREO', mensaje, archivos_adjuntos)