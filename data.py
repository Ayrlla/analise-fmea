fault_data = {
    "Não desimanta": {
        "causes": [
            {"name": "Molha", "probability": 0.7, "actions": "Secar o eletroímã"},
            {"name": "Sobrecarga", "probability": 0.3, "actions": "Substituir a bobina"}
        ],
        "actions": {
            "Molha": "Secar o eletroímã",
            "Sobrecarga": "Substituir a bobina"
        }
    },
    "Baixa imantação": {
        "causes": [
            {"name": "Fiação danificada", "probability": 0.5, "actions": "Substituir o cabo de alimentação"},
            {"name": "Núcleo desgastado", "probability": 0.5, "actions": "Substituir o núcleo"}
        ],
        "actions": {
            "Fiação danificada": "Substituir o cabo de alimentação",
            "Núcleo desgastado": "Substituir o núcleo"
        }
    },
    # Add more fault data as needed
}
