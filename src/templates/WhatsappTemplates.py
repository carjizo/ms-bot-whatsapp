class WhatsappTemplates:
    # bienvenida = {
    #     "messaging_product": "whatsapp",
    #     "to": "{phoneTo}",
    #     "type": "template",
    #     "template": {
    #         "name": "bienvenida",
    #         "language": {"code": "es"},
    #         "components": [
    #             {
    #                 "type": "header",
    #                 "parameters": [
    #                     {
    #                         "type": "image",
    #                         "image": {
    #                             "link": "https://i.ibb.co/ZzFHQ0g/presupuesto.jpg"
    #                         }
    #                     }
    #                 ]
    #             },
    #             {
    #                 "type": "body",
    #                 "parameters": [
    #                     {
    #                         "type": "text",
    #                         "text": "{userName}"
    #                     }
    #                 ]
    #             }
    #         ]
    #     }
    # }

    bienvenida = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {
            "name": "bienvenida_v2",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": "https://i.ibb.co/ZzFHQ0g/presupuesto.jpg"
                            }
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

    ingresa_monto = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {"name": "ingresa_monto","language": {"code": "es_MX"}}
    }