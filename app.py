import argparse
from scraper.scraper import get_property_data
import json

parser = argparse.ArgumentParser(
                    prog='RealityRealtyScraper',
                    description='Proyecto para la obtención de datos de anuncios para el sitio web realityrealtypr.com.')

parser.add_argument('tipo_propiedad', 
                    type=str,
                    help="Tipo de propiedades de interés ('HOUSE' para casa o 'APARTMENT' para apartamento)"
                    )

parser.add_argument('n_pagina',
                    type=int,
                    help='Número de pagina para la cual extraer información, iniciando desde el cero (0)'
                    )
 
parser.add_argument('archivo_destino', 
                    type=str,
                    help="Ruta relativa de archivo de salida con la información obtenida."
                    )

def main():
    args = vars(parser.parse_args())
    scraped_data = get_property_data(
        property_type=args["tipo_propiedad"],
        n_page=args["n_pagina"]
    )
    json_data = json.dumps(scraped_data, indent=4, ensure_ascii=False)
    with open(args['archivo_destino'],"+w", encoding="utf-8") as file:
        file.write(json_data)
    print(f"Scrape data saved on '{args['archivo_destino']}'.")

if __name__ == "__main__":
    main()