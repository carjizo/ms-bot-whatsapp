class WhatsappTemplates:
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

    resumen_presupuesto_v2 = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {
            "name": "resumen_presupuesto",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "{ultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{ingresosUltimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{gastosUltimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{resumenUltimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{penultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{ingresosPenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{gastosPenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{resumenPenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{antiPenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{ingresosAntipenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{gastosAntipenultimoPeriodo}"
                        },
                        {
                            "type": "text",
                            "text": "{resumenAntipenultimoPeriodo}"
                        },
                    ]
                }
            ]
        }
    }

    resumen_presupuesto = {
        "messaging_product": "whatsapp",
        "to": "{phoneTo}",
        "type": "template",
        "template": {
            "name": "resumen_presupuesto_v2",
            "language": {"code": "es"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "{resumenPresupuesto}"
                        }
                    ]
                }
            ]
        }
    }