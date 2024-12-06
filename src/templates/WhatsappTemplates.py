class WhatsappTemplates:
    bienvenida = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {
            "name": "bienvenida",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "text": f"https://www.google.com/imgres?q=calculadora%20de%20distancia%20entre%20dos%20puntos&imgurl=https%3A%2F%2Fi0.wp.com%2Flasmatesfaciles.com%2Fwp-content%2Fuploads%2F2023%2F03%2Fimage-7.png%3Fresize%3D840%252C806%26ssl%3D1&imgrefurl=https%3A%2F%2Flasmatesfaciles.com%2F2023%2F03%2F09%2Fdistancia-entre-dos-puntos%2F&docid=wa2JHx97ooX0TM&tbnid=Sws5FDDPjK7PfM&vet=12ahUKEwi36-XP4JKKAxWPCrkGHU_QEnAQM3oECFIQAA..i&w=840&h=806&hcb=2&ved=2ahUKEwi36-XP4JKKAxWPCrkGHU_QEnAQM3oECFIQAA"
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "{userName}"
                        }
                    ]
                }
            ]
        }
    }

    message_dev = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {"name": "message_dev","language": {"code": "es_MX"}}
    }