class Test(unittest.TestCase):

  def test_ajustar_gastos_con_1_devuelve_una_copia_identica_del_dataframe(self):
    original = pd.DataFrame([{
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
        'other_expenses': 0.0}])
    self.assertEquals(ajustar_gastos(original), original)
        