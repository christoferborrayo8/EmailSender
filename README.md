# EmailSender

El objetivo de este código es enviar un correo con archivos adjuntos a cada miembro de un grupo específico de trabajo. Estos grupos son leidos por medio de un CSV en el cual se obtiene el carné del integrante, su nombre, su número de grupo y su correo.

Dependiendo del número del grupo, se enviará un archivo diferente y al mismo tiempo se enviará un archivo general a todos.

El código está realizado de tal forma que no importa el orden en el cual los datos lleguen, siempre que los datos tengan estas 4 características funcionará.

Como recomendación, si se utiliza el smtp de Google (Gmail) habilitar las contraseñas de aplicación y utilizar esa contraseña como acceso a este correo.

Para más información visitar:
https://support.google.com/accounts/answer/185833?visit_id=638322489408911794-832047927&p=InvalidSecondFactor&rd=1