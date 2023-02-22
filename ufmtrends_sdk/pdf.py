import os
from fpdf import FPDF
import requests

class PDF(FPDF):
    # CURR_COL = 0 # This is for "static" variables


    def __init__(self, orientation, unit, format, 
                    default_label="Informe_Guatemala.png", 
                    secondary_label="Market_Trends.png", 
                    title_color=(0, 201, 245),
                    delete_temp=True,
                    tmp="./tmp/mytemp"):
        super().__init__(orientation, unit, format) 
        self.default_label = default_label
        self.secondary_label = secondary_label
        self.title_color = title_color

        self.CURR_COL = 0
        self.IS_COVER = True
        # FPDF.accept_page_break = self._accept_page_break
        # FPDF.add_page = self._add_page
        # FPDF.footer = self._footer
        
        self.TMP = tmp#"./tmp/mytemp"
        os.makedirs(self.TMP, exist_ok=True)
        filelist=os.listdir(self.TMP)
        self.DELETE_TEMP = delete_temp#True
        if self.DELETE_TEMP:
            for file in filelist:
                os.remove(os.path.join(self.TMP,file))

        # Letter
        self.WIDTH = 215.9
        self.HEIGHT = 279.4
        self.LEFT_COL_X = 11
        self.RIGHT_COL_X = self.WIDTH/2+5
        self.CURR_COL = 0
        # https://www.geeksforgeeks.org/method-overriding-in-python/
        # self.pdf = FPDF('P', 'mm', 'Letter') 

    def accept_page_break(self):
        if self.CURR_COL == 0:
            # self.set_left_margin(self.RIGHT_COL_X)
            # self.set_y(10)
            # self.CURR_COL = 1
            # print("switch right")
            self.set_right_col()
            return False
        else:
            # self.set_x(self.LEFT_COL_X)
            # self.set_left_margin(self.LEFT_COL_X)
            # self.CURR_COL = 0
            # print("switch left")
            self.set_left_col()
            return True
    def add_page(self, orientation='', isCover=False):
        print("changing cover to ", isCover)
        # https://www.geeksforgeeks.org/method-overriding-in-python/
        super().add_page(orientation=orientation)
        self.IS_COVER = isCover
        print("Adding image...")
        brand_image =  (self.secondary_label 
                        if self.page_no() % 2 == 0 
                        else self.default_label)
        self.image(brand_image, 5, 5, self.WIDTH)

    def footer(self):
        print("is cover? ", self.IS_COVER)
        if self.IS_COVER: return
        # # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        self.set_x(-9)
        # # Setting font: helvetica italic 8
        # self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.set_text_color(128, 128, 128)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"{self.page_no()}")

    def set_right_col(self):
        self.set_left_margin(self.RIGHT_COL_X)
        self.set_y(10)
        self.CURR_COL = 1
        print("switch right")
    def set_left_col(self):
        self.set_x(self.LEFT_COL_X)
        self.set_left_margin(self.LEFT_COL_X)
        self.CURR_COL = 0
        print("switch left")

    def insert_chart(self, name, id, x, y, width, px_width, px_height='auto'):
        url = f"https://api.datawrapper.de/v3/charts/{id}/export/png?unit=px&mode=rgb&width={px_width}&height={px_height}&plain=false&scale=1&zoom=2&download=false&fullVector=false&ligatures=true&transparent=false&logo=auto&dark=false&borderWidth=0"
        print(url)
        # url = "https://api.datawrapper.de/v3/charts/XPerj/export/PNG?unit=px&mode=rgb&width=400&height=300&plain=false&scale=1&zoom=2&download=false&fullVector=false&ligatures=true&transparent=false&logo=auto&dark=false"
        token = os.getenv("DATAWRAPPER_API_TOKEN")

        headers = {"Accept": "image/png", "Authorization": f"Bearer {token}"}

        image_path = f'{self.TMP}/{name}.png'
        if os.path.exists(image_path) == False:
            response = requests.request("GET", url, headers=headers)
            file = open(image_path, 'wb')
            file.write(response.content)
            file.close()
        self.image(image_path, x, y, width)
        self.ln(5)

    def insert_420x280_chart(self, name, id):
        self.insert_chart(name, id, 
                            None,#LEFT_COL_X, 
                            None,#row_offset, 
                            self.WIDTH/2-15,
                            px_width=420, px_height=280)
                            
    def insert_420xauto_chart(self, name, id):
        self.insert_chart(name, id, 
                            None,#LEFT_COL_X, 
                            None,#row_offset, 
                            self.WIDTH/2-15,
                            px_width=420, px_height='auto')

    def insert_440x292_chart(self, name, id, x_scale=1, y_scale=1):
        self.insert_chart(name, id,
                            None,
                            None,
                            self.WIDTH/2-15,
                            px_width=440*x_scale, px_height=292*y_scale)


    def insert_500x292_chart(self, name, id, x_scale=1, y_scale=1):
        self.insert_chart(name, id,
                            None,
                            None,
                            self.WIDTH/2-15,
                            px_width=500*x_scale, px_height=292*y_scale)

    def insert_500x292_chart(self, name, id, x_scale=1, y_scale=1):
        self.insert_chart(name, id,
                            None,
                            None,
                            self.WIDTH/2-15,
                            px_width=650*x_scale, px_height="auto")

    def insert_WIDTHxHEIGHT_chart(self, name, id, width, height, x_scale=1, y_scale=1):
        self.insert_chart(name, id,
                            None,
                            None,
                            self.WIDTH/2-15,
                            px_width=width*x_scale, px_height=height*y_scale)                            

    def insert_title(self, text):
        self.set_font('Arial', 'B', 20)
        c = self.title_color
        self.set_text_color(c[0], c[1], c[2])
        self.multi_cell(w=self.WIDTH/2-15, h=7, txt=text,
                    align='L')
        self.ln(5)

    def insert_subtitle1(self, text):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 12)        
        self.multi_cell(w=self.WIDTH/2-15, h=5, txt=text, align='J')
        self.ln(5)

    def insert_subtitle2(self, text):
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 12)
        self.multi_cell(w=self.WIDTH/2-15, h=5, txt=f'          {text}', align='J')

    def insert_paragraph(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(w=self.WIDTH/2-15, h=4.5, txt=text,
                    align='J')
        self.ln(5)


    def write_pdf_test(self):
        self.set_top_margin(10)
        self.set_left_margin(10)

        self.add_page()
        self.image('PortadaTrends.PNG', 0, 0, self.WIDTH)

        self.add_page()
        self.set_font('Arial', 'B', 20)
        self.set_text_color(0, 201, 245)
        # pdf.cell(w=0, txt='Actividad económica')
        self.multi_cell(w=self.WIDTH, h=7, txt='Actividad económica',
                    align='L')

        
        self.insert_chart('crecimiento-pib-guatemala', 
                    'AZ9gl',
                    11, 25, self.WIDTH/2-15,
                    px_width=420, px_height=280)

                    
        self.output(f'{self.TMP}/pdf-test.pdf', 'F')
        print('pdf written successfully')

    def write_pdf(self):
        # Add a Unicode free font
        # pdf.add_font('MyriadPro', '', 'Myriad-Pro-Regular.ttf', uni=True)

        
        # SET MARGINS
        self.set_top_margin(10)
        self.set_left_margin(10)

        # UFM MARKET TRENDS COVER
        self.add_page(isCover=True)
        self.image('PortadaTrends.PNG', 0, 0, self.WIDTH)

        self.add_page()
        self.image('Market_Trends.png', 5, 5, self.WIDTH)

        # ECONOMIC ACTIVITY
        self.insert_title(text='Actividad económica \ny empleo')
        
        self.insert_subtitle1(text='1. Actividad económica')

        self.insert_subtitle2(text='a. PIB')

        self.insert_paragraph('''El PIB es el valor añadido de los bienes y servicios producidos en un país. El Banguat utiliza una "base fija" atada a los precios del año 2013 para calcular el cambio del PIB año con año. El problema de usar una base fija es que, cuánto más desactualizado sea el año base, más graves son los problemas con la estimación del PIB.''')
        
        # https://app.datawrapper.de/chart/AZ9gl/publish
        self.insert_420x280_chart('crecimiento-pib-guatemala', 'AZ9gl')

        self.insert_subtitle2(text='b. IMAE')

        self.insert_paragraph(text='Los datos del PIB se publican con bastante retraso, por ello el Banco de Guatemala publica un Índice Mensual de Actividad Económica (IMAE). Aunque el IMAE es menos preciso que el PIB, puede darnos una idea mucho más actualizada del estado de la economía.')

        # https://app.datawrapper.de/chart/XPerj/publish
        self.insert_420x280_chart('crecimiento-economico-imae', 'XPerj')

        self.ln(15)

        self.insert_subtitle2(text='c. Crecimiento PIB Guatemala \n              por sectores')

        # self.ln(5)
        self.insert_paragraph(text='Entre los sectores con mayor crecimiento, destaca la acelerada recuperación del sector de hoteles y restaurantes. Cabe mencionar que el sector de salud se ha consolidado entre los de mayor crecimiento durante los últimos dos años.')

        # https://app.datawrapper.de/chart/rFyKJ/publish
        self.insert_420xauto_chart('sectores-mayor-crecimiento', 'rFyKJ')

        self.insert_paragraph(text='Por su parte, entre los sectores con menor crecimiento, destaca el sector de agricultura en la última posición. Aunque este sector fue resiliente durante la crisis, posterior a la recuperación económica, su tasa de crecimiento vuelve a estar muy por debajo del ritmo de crecimiento de la economía total.')

        # https://app.datawrapper.de/chart/3suhL/publish
        self.insert_420xauto_chart('sectores-menor-crecimiento', '3suhL')
        # https://app.datawrapper.de/chart/I00QJ/publish
        self.insert_420x280_chart('crecimiento-pib-hoteles', 'I00QJ')

        # https://app.datawrapper.de/chart/tzxRS/publish
        self.insert_420x280_chart('crecimiento-pib-agricultura', 'tzxRS')

        # INFLATION AND PRICES
        self.insert_title(text='Inflación y precios')

        self.insert_subtitle1(text='1. Agregados monetarios')

        self.insert_subtitle2(text='a. Quetzal')

        self.insert_paragraph('''La base monetaria de dinero que emite el banco central. M2 es el dinero del banco central en manos del público más los depósitos monetarios a corto plazo.''')

        # https://app.datawrapper.de/chart/5nqdD/publish
        self.insert_440x292_chart('agregados-monetarios-quetzal', '5nqdD')

        self.insert_subtitle2(text='b. Quetzal y dólar')
        self.insert_paragraph('''La base monetaria amplia incluye las monedas y billetes en moneda extranjera. El agregado monetario M3 toma en cuenta también los depósitos en moneda extranjera.''')

        # https://app.datawrapper.de/chart/FNxZd/publish
        self.insert_440x292_chart('agregados-monetarios-quetzal-y-dolar', 'FNxZd')
        
        self.insert_subtitle1(text='2. Índice de precios al consumidor')
        
        self.insert_paragraph('''El índice de precios al consumidor nos permite monitorear el estado de la inflación. La inflación subyacente excluye los efectos del precio de la energía.''')

        # https://app.datawrapper.de/chart/a90Cn/publish
        self.insert_440x292_chart('crecimiento-precios-consumo', 'a90Cn')
                
        # https://app.datawrapper.de/chart/9tgGq/publish
        self.insert_440x292_chart('crecimiento-inflacion-subyacente', '9tgGq')

        # self.add_page()
        # self.set_left_col()
        self.insert_title(text='Sector externo')

        self.insert_subtitle1(text='1. Balanza por cuenta corriente')

        self.insert_paragraph('''La balanza por cuenta corriente recoge el comercio de bienes y servicios, las remesas y donaciones y los rendimientos de inversiones en el extranjero. Para Guatemala sólo las dos primeras son realmente importantes.''')

        # https://app.datawrapper.de/chart/Y4gDq/publish
        self.insert_420x280_chart('balanza-cuenta-corriente', 'Y4gDq')

        self.insert_paragraph('''Desglosemos las sub-balanzas más importantes de la balanza por cuenta corriente.''')

        self.insert_subtitle2(text='a. Balanza comercial o de bienes \n              (exportaciones e importaciones)')

        self.insert_paragraph('''El volumen de la balanza de bienes representa la magnitud total del comercio internacional guatemalteco.''')

        # https://app.datawrapper.de/chart/x7ZN1/publish
        self.insert_420x280_chart('balanza-comercial', 'x7ZN1')

        self.insert_subtitle2(text='b. Remesas \n              (balanza ingreso secundario)')
        self.insert_paragraph('''La cuantía de las remesas creció a pasos agigantados durante la segunda década del siglo XXI, sobrepasando a las exportaciones y dejado muy atrás a la IED.''')

        # https://app.datawrapper.de/chart/91spl/publish
        self.insert_440x292_chart('remesas-exportaciones-IED', '91spl')

        self.insert_subtitle1(text='2. Cuenta financiera')
        self.insert_paragraph('''La cuenta financiera indica si el país recibe (-) o proporciona (+) financiación neta al exterior.''')

        # https://app.datawrapper.de/chart/9ZBlH/publish
        self.insert_420x280_chart('balanza-financiera', '9ZBlH')

        self.insert_subtitle1(text='3. Inversión extranjera directa')
        self.insert_paragraph('''La IED constituye un porcentaje muy pequeño del PIB. Prácticamente no hay nueva inversión en Guatemala.''')
        #  El dato de 2021 es un valor atípico y se debe a la compra del 45% de acciones de Tigo por parte''')# de Millicom por un valor de 2200 millones de dólares.''')

        # https://app.datawrapper.de/chart/iVVu6/publish
        self.insert_420x280_chart('desglose-IED', 'iVVu6')

        self.insert_subtitle1(text='4. Tipo de cambio')
        self.insert_paragraph('''A pesar de la inflación, el tipo de cambio se ha mantenido estable. Banguat ha logrado esto reajustando la emisión de quetzales y la compra de dólares en el mercado cambiario.''')

        # https://app.datawrapper.de/chart/WsMA2/publish
        self.insert_440x292_chart('tipo-cambio', 'WsMA2')
        
        self.insert_subtitle1(text='5. Grado de dolarización economía')
        
        self.insert_paragraph('''El grado de dolarización de la economía nos permite entender el nivel de confianza que el sector privado tiene en la moneda nacional.''')

        # https://app.datawrapper.de/chart/l2SIz/publish
        self.insert_440x292_chart('dolarizacion-economia', 'l2SIz')


        self.insert_title(text='Sistema bancario')
        self.insert_subtitle1(text='1. Estabilidad sistema bancario')

        self.insert_subtitle2(text='a. Capitalización sistema bancario')

        self.insert_paragraph(text='''La razón de capital del sistema bancario (con respecto a activos u obligaciones) nos informa de la capacidad del sector de absorber pérdidas por posibles impagos sin afectar a la estabilidad del sistema financiero.''')

        # https://app.datawrapper.de/chart/Q4KsP/publish
        self.insert_440x292_chart('sisbancario-capitalizacion', 'Q4KsP')

        self.insert_subtitle2(text='b. Calidad de la cartera de crédito')
        self.insert_paragraph('''La razón de cobertura de préstamos morosos nos informa de la capacidad que tienen los bancos para absorber pérdidas futuras.''')

        # https://app.datawrapper.de/chart/uAzEC/publish
        self.insert_440x292_chart('cartera-creditos-vencida', 'uAzEC')

        # https://app.datawrapper.de/chart/Kct9w/publish
        self.insert_440x292_chart('cobertura-creditos-riesgo', 'Kct9w')


        self.insert_subtitle2(text='c. Rentabilidad sistema bancario')
        self.insert_paragraph('''Los indicadores de rentabilidad bancaria nos informan sobre la eficiencia del sector y, también, posibles problemas o sobrecalentamiento financiero.''')

        # https://app.datawrapper.de/chart/x9Ev0/publish
        self.insert_440x292_chart('sisbancario-retorno-capital', 'x9Ev0')


        # https://app.datawrapper.de/chart/H9jwc/publish
        self.insert_440x292_chart('sisbancario-retorno-activos', 'H9jwc')

        self.insert_subtitle1(text='2. Extensión de crédito por sector')
        self.insert_paragraph('''La composición sectorial del crédito nos puede dar una idea del potencial crecimiento futuro de diferentes sectores económicos.''')

        # https://app.datawrapper.de/chart/yGNBT/publish
        self.insert_420x280_chart('crecimiento-credito-finanzasinmuebles', 'yGNBT')

        # https://app.datawrapper.de/chart/CmCpq/publish
        self.insert_440x292_chart('crecimiento-credito-sectores2', 'CmCpq', y_scale=1.55)
        # self.insert_420xauto_chart('crecimiento-credito-sectores2', 'CmCpq')

        self.insert_title(text='Fiscalidad')
        # https://app.datawrapper.de/chart/VQcBL/publish
        self.insert_chart('deficit-porcentaje-ingreso', 'VQcBL',
                            None,
                            None, 
                            self.WIDTH/2-15,
                            px_width=500,
                            px_height=292)
        # https://app.datawrapper.de/chart/Jg2r7/publish
        # self.insert_chart('deuda-porcentaje-ingreso', 'Jg2r7')
        self.insert_chart('deuda-porcentaje-ingreso', 'Jg2r7',
                            None,
                            None, 
                            self.WIDTH/2-15,
                            px_width=500,
                            px_height=292)


        self.add_page(isCover=True)
        self.image('ContraPortadaTrends.PNG', 0, 0, self.WIDTH)


        self.output(f'{self.TMP}/pdf.pdf', 'F')
        print('pdf written successfully')


def application():
    # write_pdf_test()
    engine = PDF('P', 'mm', 'Letter')
    engine.write_pdf()

if __name__ == '__main__':
    application()