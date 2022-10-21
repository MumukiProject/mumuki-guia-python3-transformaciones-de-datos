class Test(unittest.TestCase):
  
  def test_visitas_previas_por_region_es_un_DataFrame(self):
    self.assertEquals(type(visitas_previas_por_region), pd.DataFrame)
      

  def test_description_example(self):
    self.assertTrue(True)