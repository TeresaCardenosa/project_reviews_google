import pandas as pd

# Lista de hospitales para tipología 
hospital = ['Hospital Universitari Sagrat Cor',
            'Hospital Quirónsalud del Vallés', 
            'Hospital Quirónsalud Son Verí',
            'Hospital El Pilar – Consultas Externas Alfonso XII',
            'Hospital El Pilar – Consultas Externas Balmes',
           'Hospital Quirónsalud Lugo',
           'Hospital Quirónsalud Valle del Henares (Torrejón de Ardoz)',
           'Hospital Materno-Infantil Quirónsalud',
           'Hospital Quirónsalud Vida',
           'Hospital Quirónsalud Badalona',
           'Hospital Universitario Quirónsalud Madrid',
           'Hospital Quirónsalud A Coruña', 
            'Hospital Quirónsalud Málaga',
           'Hospital Quirónsalud Tenerife', 
            'Hospital Quirónsalud Torrevieja',
           'Hospital Quirónsalud Toledo',
           'Hospital Quirónsalud Miguel Domínguez',
           'Hospital Quirónsalud Clideba', 
            'Hospital Quirónsalud Ciudad Real',
           'Hospital Ruber Internacional', 
            'Hospital Quirónsalud Costa Adeje',
           'Hospital Quirónsalud Huelva', 
            'Hospital Quirónsalud Palmaplanas',
           'Hospital Quirónsalud Sur', 
            'Hospital Quirónsalud Murcia',
           'Hospital Quirónsalud Valencia', 
            'Hospital Quirónsalud Albacete',
           'Hospital Quirónsalud Marbella',
           'Hospital Quironsalud Sagrado Corazón',
           'Hospital Universitario Fundación Jiménez Díaz',
           'Hospital Universitari General de Catalunya',
           'Hospital Universitario General de Villalba',
           'Hospital  Universitario La Luz',
           'Hospital Quirónsalud Córdoba',
           'Hospital Quirónsalud Infanta Luisa',
           'Hospital Quirónsalud Santa Cristina',
           'Hospital Quirónsalud Bizkaia',
           'Hospital Quirónsalud Campo de Gibraltar',
           'Hospital Universitario Ruber Juan Bravo (C/Juan Bravo, 49)',
           'Hospital Quirónsalud San José',
           'Hospital Quirónsalud Cáceres', 
            'Hospital El Pilar',
           'Hospital Quirónsalud Vitoria', 
            'Hospital Quirónsalud Zaragoza',
           'Hospital Universitario Ruber Juan Bravo (C/ Juan Bravo, 39)',
           'Hospital Universitario Infanta Elena',
           'Hospital Universitari Dexeus',
           'Hospital Universitario Rey Juan Carlos',
           'Hospital Quirónsalud Barcelona', 
           'Centro Médico Teknon', 
           'Policlínica Gipuzkoa', 
           'IERA Quirónsalud',
           'IERA - Lisboa',
           'Olympia - Grupo Quirónsalud',
           'Quirónsalud Alicante',
           'Centro de Protonterapia Quirónsalud', 
            'Clínica Rotger']

# Lista de centros médicos para tipología 
centro = ['Centro Médico Quirónsalud Murcia',
       'Centro Médico Quirónsalud Sevilla Este',
       'Centro de especialidades Pontones',
       'Centro de especialidades Argüelles',
       'Centro de especialidades Cristo Rey',
       'Centro de especialidades Navalcarnero',
       'Centro de especialidades Villaviciosa de Odón',
       'Centro Médico Ruber Juan Bravo',
       'Centro Médico Quirónsalud Digest Marti Pujol',
       'Centro Médico Quirónsalud Algeciras',
       'Centro Médico Quirónsalud Parque Litoral',
       'Centro Médico Quirónsalud Marbella',
       'Centro Médico Quirónsalud Guadalete',
       'Centro Médico Quirónsalud Condes de Bustillo',
       'Centro Médico Quirónsalud Espartinas',
       'Centro Médico Quirónsalud Blasco Ibañez',
       'Centro Médico Quirónsalud Artes Gráficas',
       'Centro M. Quirónsalud Almendralejo',
       'Centro M. Quirónsalud Don Benito',
       'Centro Médico Quirónsalud Nuredduna',
       'Centro Médico Quirónsalud Inca',
       'Centro Médico Quirónsalud Manacor',
       'Centro Médico Quirónsalud Palmanova',
       'Centro Médico Quirónsalud Dígest Laietania',
       'Centro Médico Quirónsalud Costa del Sol',
       'Centro Médico Quirónsalud Severo Ochoa',
       'Centro Médico Quirónsalud Plaza Madroño',
       'Centro Médico Quirónsalud Mercado de Colón',
       'Centro Médico Quirónsalud Gran Alacant',
       'Ruber Internacional Centro Médico Masó',
       'Centro Médico Quirónsalud Elche',
       'Centro Médico Vida La Laguna',
       'Centro Médico Quirónsalud Los Cristianos',
       'Centro médico Quirónsalud Vida Candelaria',
       'Centro Médico Vida - Santa Úrsula',
       'Centro Médico Vida - Icod de los Vinos',
       'Centro Médico Vida Tejina',
       'Centro Médico Vida - Puerto de la Cruz',
       'Centro Médico Vida - Los Realejos',
       'Centro médico Quirónsalud Plaza Lodares ',
       'Centro Médico Quirónsalud',
       'Centro Médico Quirónsalud Valdebebas',
       'Centro Médico Quirónsalud Pontevedra',
       'Centro Médico Ruber Internacional Paseo Habana',
       'Centro Médico Quirónsalud Toledo', 
       'Centro Médico Quirónsalud Aribau',
       'Centro Médico Quirónsalud Aljarafe',
       'Centro Médico Quirónsalud Alameda',
       'Centro Médico Quirónsalud Manuel Siurot',
       'Centro Médico Quirónsalud Los Remedios',
       'Centro Médico Quirónsalud Mairena',
       'Centro Médico Quirónsalud Málaga',
       'Centro Médico Quirónsalud Nervión',
       'Centro Médico Quirónsalud Plaza Euskadi',
       'Centro Médico Quirónsalud Tres Cantos',
       'Centro Médico Quirónsalud Valle del Henares (Alcalá de Henares)',
       'Centro Médico Quirónsalud A Coruña',
       'Centro Médico Quirónsalud Ferrol',
       'Centro Médico Quirónsalud Fuengirola',
       'Centro Médico Quirónsalud Mérida',
       'Centro Médico Quirónsalud Orihuela',
       'Centro Médico Quirónsalud Puertollano',
       'Centro Médico Quirónsalud Tenerife',
        'Instituto de Neuro-rehabilitación Quirónsalud Pontevedra',
         'Centre Mèdic Quirónsalud Rubí',
         'Centre Mèdic Quirónsalud Badalona Arbres',
         'Hospital de Día Quirónsalud Huesca',
       'Hospital de Día Quirónsalud Ave María',
       'Hospital de Día Quirónsalud Playa de Muro',
       'Hospital de Día Quirónsalud Talavera',
       'Hospital De Día Quirónsalud Zaragoza',
       'Hospital de Día Quirónsalud Donostia',
         'Clínica Quirónsalud Alcázar']

# Lista de Otros para tipología 
otros = ['Instituto Oncológico Quirónsalud Zaragoza',
       'Grupo Hospitalario Quirónsalud',
        'Centro de Rehabilitación Ruber Juan Bravo',
       'Consultas Externas Hospital Quirónsalud San José',
        'Quirónsalud Dental Inca',
       'Quirónsalud Dental Manacor', 
         'Quirónsalud Dental Kids',
        'Centro de Oftalmología Quirónsalud Marbella',
        'Centro de Rehabilitación Quirónsalud Vitoria',
        'Centro de Rehabilitación Quirónsalud Talavera',
        'Centro de Oftalmología Quirónsalud Vitoria',
         'Centro de Rehabilitación Quirónsalud Huelva',
       'Centro de Rehabilitación Quirónsalud Infanta Luisa',
        'Consultas Externas Hospital Quirónsalud Sur',
        'Laboratorio Análisis Clínicos – Hospital Universitari Dexeus',
        'Centro de Rehabilitación Quirónsalud Pontevedra',
        'Quirónsalud Dental y Unidad de Obesidad Quirónsalud Valencia',
        'Unidad de Pediatría Quirónsalud Zaragoza',
        'Unidad de la Mujer de Quirónsalud Zaragoza',
       'Instituto Oftalmológico Quirónsalud Zaragoza',
        'Instituto Oftalmológico Quirónsalud A Coruña']

# Listas de Territorios
T_publicos_Madrid = ['Centro de especialidades Pontones',
                   'Centro de especialidades Argüelles',
                   'Centro de especialidades Cristo Rey',
                   'Centro de especialidades Navalcarnero',
                   'Centro de especialidades Villaviciosa de Odón',
                     'Hospital Universitario Fundación Jiménez Díaz',
                   'Hospital Universitario General de Villalba',
                   'Hospital Universitario Infanta Elena',
                   'Hospital Universitario Rey Juan Carlos']

T_corporativo = ['Grupo Hospitalario Quirónsalud']

TRI = ['Ruber Internacional Centro Médico Masó',
       'Hospital Ruber Internacional',
       'Centro Médico Ruber Internacional Paseo Habana']

T1 = ['Centro de Protonterapia Quirónsalud',
      'Hospital Universitario Quirónsalud Madrid',
      'Hospital Quirónsalud Valle del Henares (Torrejón de Ardoz)',
      'Centro Médico Quirónsalud Valle del Henares (Alcalá de Henares)',
      'Hospital Quirónsalud San José',
      'Olympia - Grupo Quirónsalud',
      'Hospital Universitario Ruber Juan Bravo (C/ Juan Bravo, 39)',
      'Hospital Universitario Ruber Juan Bravo (C/Juan Bravo, 49)',
      'Hospital Quirónsalud Sur', 
      'Hospital  Universitario La Luz',
      'Centro Médico Ruber Juan Bravo',
      'Centro de Rehabilitación Ruber Juan Bravo',
      'Consultas Externas Hospital Quirónsalud San José',
       'Centro Médico Quirónsalud Valdebebas',
      'Consultas Externas Hospital Quirónsalud Sur',
      'Centro Médico Quirónsalud Tres Cantos']

T_Barcelona_Valles = ['Hospital Universitari Sagrat Cor',
       'Hospital Quirónsalud del Vallés',
      'Hospital Universitari General de Catalunya']

T2 = ['Hospital Quirónsalud Badalona',
       'Centro Médico Teknon',
       'Hospital El Pilar',
       'Hospital Universitari Dexeus', 
      'Hospital Quirónsalud Barcelona',
      'Centre Mèdic Quirónsalud Rubí',
       'Centre Mèdic Quirónsalud Badalona Arbres',
       'Centro Médico Quirónsalud Digest Marti Pujol',
       'Hospital El Pilar – Consultas Externas Alfonso XII',
       'Hospital El Pilar – Consultas Externas Balmes',
       'Centro Médico Quirónsalud Dígest Laietania',
       'Centro Médico Quirónsalud Aribau',
     'Instituto Oncológico Quirónsalud Zaragoza',
       'Hospital de Día Quirónsalud Huesca',
       'Unidad de Pediatría Quirónsalud Zaragoza',
       'Unidad de la Mujer de Quirónsalud Zaragoza',
       'Hospital De Día Quirónsalud Zaragoza',
     'Hospital Quirónsalud Zaragoza',
     'Instituto Oftalmológico Quirónsalud Zaragoza',
     'Laboratorio Análisis Clínicos – Hospital Universitari Dexeus']

T3 = ['Centro Médico Quirónsalud Sevilla Este',
       'Centro Médico Quirónsalud Algeciras',
       'Centro Médico Quirónsalud Parque Litoral',
       'Centro Médico Quirónsalud Marbella',
       'Centro Médico Quirónsalud Guadalete',
       'Centro Médico Quirónsalud Condes de Bustillo',
       'Centro Médico Quirónsalud Espartinas',
       'Centro de Oftalmología Quirónsalud Marbella',
       'Centro Médico Quirónsalud Costa del Sol',
       'Centro Médico Quirónsalud Aljarafe',
       'Hospital de Día Quirónsalud Ave María',
       'Centro Médico Quirónsalud Alameda',
       'Centro Médico Quirónsalud Manuel Siurot',
       'Centro Médico Quirónsalud Los Remedios',
       'Centro Médico Quirónsalud Mairena',
       'Centro Médico Quirónsalud Málaga',
       'Centro Médico Quirónsalud Nervión',
       'Centro Médico Quirónsalud Fuengirola',
     'Hospital Materno-Infantil Quirónsalud',
       'Hospital Quirónsalud Málaga', 'Hospital Quirónsalud Huelva',
       'Hospital Quirónsalud Marbella',
       'Hospital Quironsalud Sagrado Corazón',
       'Hospital Quirónsalud Córdoba',
       'Hospital Quirónsalud Infanta Luisa',
       'Hospital Quirónsalud Campo de Gibraltar',
     'Centro de Rehabilitación Quirónsalud Huelva',
       'Centro de Rehabilitación Quirónsalud Infanta Luisa',
     'Centro Médico Quirónsalud']

T4 = ['Centro Médico Quirónsalud Murcia',
       'Centro Médico Quirónsalud Blasco Ibañez',
       'Centro Médico Quirónsalud Artes Gráficas',
       'Centro Médico Quirónsalud Severo Ochoa',
       'Centro Médico Quirónsalud Mercado de Colón',
       'Centro Médico Quirónsalud Gran Alacant',
       'Centro Médico Quirónsalud Elche',
       'Centro Médico Quirónsalud Orihuela',
      'Hospital Quirónsalud Torrevieja', 'Quirónsalud Alicante',
       'Hospital Quirónsalud Murcia', 'Hospital Quirónsalud Valencia',
      'Quirónsalud Dental y Unidad de Obesidad Quirónsalud Valencia']

T5 = ['Policlínica Gipuzkoa', 'Hospital Quirónsalud Bizkaia',
       'Hospital Quirónsalud Vitoria',
      'Centro Médico Quirónsalud Plaza Euskadi',
       'Hospital de Día Quirónsalud Donostia',
      'Centro de Rehabilitación Quirónsalud Vitoria',
       'Centro de Oftalmología Quirónsalud Vitoria']

T6 = ['Centro de Rehabilitación Quirónsalud Talavera',
      'Centro Médico Quirónsalud Plaza Madroño',
       'Centro médico Quirónsalud Plaza Lodares ',
       'Centro Médico Quirónsalud Toledo', 'Clínica Quirónsalud Alcázar',
       'Centro Médico Quirónsalud Puertollano',
       'Hospital de Día Quirónsalud Talavera',
      'Hospital Quirónsalud Toledo', 'Hospital Quirónsalud Ciudad Real',
       'Hospital Quirónsalud Albacete',
       'Hospital Quirónsalud Santa Cristina']

T7 = ['IERA Quirónsalud', 'IERA - Lisboa',
       'Centro M. Quirónsalud Almendralejo',
       'Centro M. Quirónsalud Don Benito',
       'Centro Médico Quirónsalud Mérida',
      'Hospital Quirónsalud Clideba', 'Hospital Quirónsalud Cáceres']

T8 = ['Quirónsalud Dental Inca', 'Quirónsalud Dental Manacor',
       'Quirónsalud Dental Kids',
     'Hospital Quirónsalud Son Verí',
       'Hospital Quirónsalud Palmaplanas', 'Clínica Rotger',
      'Centro Médico Quirónsalud Nuredduna',
       'Centro Médico Quirónsalud Inca',
       'Centro Médico Quirónsalud Manacor',
       'Centro Médico Quirónsalud Palmanova',
       'Hospital de Día Quirónsalud Playa de Muro']

T9 = ['Centro Médico Vida La Laguna',
       'Centro Médico Quirónsalud Los Cristianos',
       'Centro médico Quirónsalud Vida Candelaria',
       'Centro Médico Vida - Santa Úrsula',
       'Centro Médico Vida - Icod de los Vinos',
       'Centro Médico Vida Tejina',
       'Centro Médico Vida - Puerto de la Cruz',
       'Centro Médico Vida - Los Realejos',
       'Centro Médico Quirónsalud Tenerife',
      'Hospital Quirónsalud Vida', 'Hospital Quirónsalud Tenerife',
       'Hospital Quirónsalud Costa Adeje']

T10 = ['Instituto de Neuro-rehabilitación Quirónsalud Pontevedra',
       'Centro de Rehabilitación Quirónsalud Pontevedra',
       'Instituto Oftalmológico Quirónsalud A Coruña',
       'Centro Médico Quirónsalud Pontevedra',
       'Centro Médico Quirónsalud A Coruña',
       'Hospital Quirónsalud Lugo', 'Hospital Quirónsalud A Coruña',
       'Hospital Quirónsalud Miguel Domínguez',
      'Centro Médico Quirónsalud Ferrol']


def read_excel():
    '''
    Lee un archivo Excel y devuelve un dataframe. 
    Input: pregunta al usuario la ubicación del archivo, la hoja a extraer, el número de fila donde están los nombres
    de las columnas. 
    Ouput: objeto dataframe
    '''
    try:
        file_location = input('Ingresa la ubicación del archivo y el formato .xlsx: ')
        sheet = int(input('Ingresa el índice de la hoja a exportar: '))
        header_row = int(input('Ingresa el número de la fila que contiene los nombres de las columnas: '))
        df = pd.read_excel(file_location, sheet_name=sheet, header=header_row)
        print(f'DataFrame generado con éxito, hay un total de ', len(df), f' reseñas.')
        return df
    except: 
        print("Error al leer el archivo")
    
def eliminar_columnas(df):
    '''
    Del DataFrame elimina las columnas que están en la lista drop_cols
    Input: dataframe
    Output: dataframe sin columnas de la lista
    '''
    drop_cols = ['Business Id',
             'Código del establecimiento',
             'Plataforma',
             'author', 
             'Eliminado', 
             'Zona horaria', 
             'Fecha de la respuesta', 
             'Respuesta', 
             'Modelo utilizado', 
             'Recomendado',
             'Fecha de la respuesta.1', 
             'Respuesta.1', 
             'Modelo utilizado.1',
             'Número de comentarios', 
             'rating.1', 
             'Fecha de la respuesta.2',
             'Respuesta.2',
                'tags'] # OJO AÑADO TAGS PORQUE SOLO 2023 LO TENÍA COMPLETO
    df = df.drop(columns=[columna for columna in drop_cols if columna in df.columns], errors='ignore')
    print(f'Eliminadas las columnas innecesarias del DataFrame. Ahora cuenta con las siguientes columnas: ', len(df.columns))
    return df

def generar_fecha(df):
    '''
    Del DataFrame comprueba si tiene una fecha de modificación y, en caso de no tenerla, asignale la fecha de creación. 
    Después elimina la columna de Fecha de creación y renombra la columna de Fecha de modificación como Fecha. 
    Input: dataframe con columna Fecha de creación y Fecha de modificación
    Output: dataframe con columna Fecha
    '''
    df['Fecha de modificación'].fillna(df['Fecha de creación'], inplace=True)
    df.drop('Fecha de creación', axis=1, inplace=True)
    df = df.rename(columns={'Fecha de modificación': 'Fecha'})
    return df


''' Funciones para generar tipografía: 
1. Dar tipografía para devolver Hospital, Centro Médico y Otros
2. Aplicar un apply sobre el dataframe '''

def dar_tipografía(establecimiento):
    if establecimiento in hospital:
        return 'Hospital'
    elif establecimiento in centro:
        return 'Centro médico'
    elif establecimiento in otros:
        return 'Otros'
    else:
        return 'Desconocido'
    
def aplicar_tipografía(df):
    df['Tipografía'] = df['Nombre del establecimiento'].apply(dar_tipografía)
    return df


''' Funciones para generar territorio. 
1. Dar territorio para devolver T1, T2, T3...
2. Aplicar un apply sobre el dataframe'''

def dar_territorio(establecimiento):
    if establecimiento in T_publicos_Madrid:
        return 'Públicos Madrid'
    elif establecimiento in T_corporativo:
        return 'Corporativo'
    elif establecimiento in TRI:
        return 'TRI'
    elif establecimiento in T1:
        return 'T1'
    elif establecimiento in T_Barcelona_Valles:
        return 'Barcelona y Vallés'
    elif establecimiento in T2:
        return 'T2'
    elif establecimiento in T3:
        return 'T3'
    elif establecimiento in T4:
        return 'T4'
    elif establecimiento in T5:
        return 'T5'
    elif establecimiento in T6:
        return 'T6'
    elif establecimiento in T7:
        return 'T7'
    elif establecimiento in T8:
        return 'T8'
    elif establecimiento in T9:
        return 'T9'
    elif establecimiento in T10:
        return 'T10'
    else:
        return 'Desconocido'

def aplicar_territorio(df):
    df['Territorio'] = df['Nombre del establecimiento'].apply(dar_territorio)
    return df

def export_csv(df):
    '''
    Pilla el DataFrame y genera un csv. 
    Input: DataFrame de argumento
    Ouput: pregunta al usuario la ubicación del archivo, el nombre que le queramos dar. 
    '''
    try:
        file_location = input('Ingresa la ubicación donde quieres guardar el archivo :')
        name = input('Ingresa el nombre que quieres dar al archivo (sin la extensión .csv) :')
        file_path = f'{file_location}/{name}.csv'
        df.to_csv(file_path, index=False)
        return f'DataFrame guardado con éxito con formato .csv'
    except: 
        print("Error al guardar el archivo")


if __name__ == '__main__':
    print('En este proceso traemos las reseñas descargadas desde Partoo y aplicaremos las transformaciones oportunas a las reseñas propias. ¡Comenzamos!')
    df = read_excel()
    print('Habemos reseñas. Vamos a aplicar las transformaciones. Por favor, espere.')
    df = eliminar_columnas(df)
    df = generar_fecha(df)
    df = aplicar_tipografía(df)
    df = aplicar_territorio(df)
    print('¡Proceso completado! Ahora simplemente guardaremos el nuevo archivo generado.')
    df = export_csv(df)
    print('Ya dispones del archivo .csv con todas las transformaciones realizadas en las reseñas descargadas de Partoo.')

