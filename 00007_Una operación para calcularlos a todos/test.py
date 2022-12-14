import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.original = pd.DataFrame([{
        'cruise_id': 10404,
        'country_id': 19,
        'country': 'Brasil',
        'date': '2020-02-06',
        'date_id': 14646,
        'port_id': 2,
        'port': 'Punta del Este',
        'total_people': 2,
        'visits_amount': 2,
        'total_expenses': 1.0,
        'tours_expenses': 5.0,
        'feed_expenses': 0.0,
        'transport_expenses': 10.0,
        'shopping_expenses': 3.0,
        'other_expenses': 2.0}])
  
  def test_ajustar_gastos_devuelve_una_copia_de_la_tabla(self):
    self.assertTrue(ajustar_gastos(self.original, 1) is not self.original, "no debería devolver el mismo dataframe, sino una copia")    

  def test_ajustar_gastos_con_1_devuelve_una_copia_identica_del_dataframe(self):
    self.assertEquals(ajustar_gastos(self.original, 1).to_dict(), self.original.to_dict())
        
        
  def test_ajustar_gastos_con_2_devuelve_un_dataframe_con_todos_los_gastos_duplicados(self):
    self.assertEquals(
      ajustar_gastos(self.original, 2)[[
        "tours_expenses", 
        "feed_expenses", 
        "transport_expenses", 
        "shopping_expenses", 
        "other_expenses"]].to_dict("records"), 
      [{
        'tours_expenses': 10.0,
        'feed_expenses': 0.0,
        'transport_expenses': 20.0,
        'shopping_expenses': 6.0,
        'other_expenses': 4.0
      }], "debería haber duplicado tours_expenses, feed_expenses, transport_expenses, shopping_expenses, other_expenses")


  def test_ajustar_gastos_no_altera_las_columnas_que_no_presentan_gastos(self):
    self.assertEquals(
      ajustar_gastos(self.original, 2)[[
        "date_id", 
        "total_people", 
        "visits_amount"
      ]].to_dict("records"), 
      [{
        'date_id': 14646,
        'total_people': 2,
        'visits_amount': 2
      }], "debería haber duplicado tours_expenses, feed_expenses, transport_expenses, shopping_expenses, other_expenses")
                                