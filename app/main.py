'''
import utils #Forma de importar los modulos en python con la palabra reservada import + nombre del modulo
data = [
  {
      'Country': 'Colombia',
      'Population':500
  },
  {
      'Country': 'Bolivia',
      'Population':300
  }
]
  
def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  
  country = input('Type Country =>')
  
  result = utils.population_by_country(data,country)
  print(result)

if __name__=='__main__':
  run()#Esta estructura le dice: que si es ejecutado el metodo main.py desde la terminal, ejecute el metodo run, pero si es ejecutado desde otro archivo, esto no se ejecutara, si no se tiene esta estructura no se corre como si fuera un script (dualidad de modulos)
'''
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] =='South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x:x['World Population Percentage'],data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()

