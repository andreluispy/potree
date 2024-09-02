import pdal

def convert_ply_to_las(input_ply, output_las):
    # Pipeline PDAL para ler o arquivo PLY e salvar como LAS
    pipeline = f"""
    [
        "{input_ply}",
        {{
            "type": "writers.las",
            "filename": "{output_las}"
        }}
    ]
    """

    # Criar e executar o pipeline
    pipeline = pdal.Pipeline(pipeline)
    pipeline.execute()

    print(f"Conversão concluída: {input_ply} -> {output_las}")

if __name__ == "__main__":
    # Caminhos dos arquivos de entrada e saída
    input_ply = "3.ply"
    output_las = "converted.las"
    
    convert_ply_to_las(input_ply, output_las)