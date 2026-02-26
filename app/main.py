import utils
import read_csv
import charts
import pandas as pd


def run():
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')

  countries_input = input('Type Countries (separated by comma) => ')
  countries = [c.strip() for c in countries_input.split(',')]

  for country_name in countries:
    result = utils.population_by_country(data, country_name)

    if len(result) > 0:
      country = result[0]
      print(country)

      labels, values = utils.get_population(country)
      charts.generate_bar_chart(country['Country'], labels, values)
    else:
      print(f'Country "{country_name}" not found')


if __name__ == '__main__':
  run()