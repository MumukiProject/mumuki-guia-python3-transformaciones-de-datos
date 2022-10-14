class Test(unittest.TestCase):

  def test_cruceros_tiene_columna_region(self):
    self.assertTrue("region" in cruceros.columns)
    

  def test_cruceros_de_brasil_son_regionales(self):
    indexado = muestra_cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[10404, "region"], "Regional")
    self.assertEquals(indexado.loc[1494, "region"], "Regional")
    self.assertEquals(indexado.loc[11099, "region"], "Regional")
    

  def test_cruceros_de_argentina_son_regionales(self):
    indexado = muestra_cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5296, "region"], "Regional")
    self.assertEquals(indexado.loc[12537, "region"], "Regional")
    self.assertEquals(indexado.loc[7237, "region"], "Regional")    
    
  def test_cruceros_de_uruguay_son_nacionales(self):
    indexado = muestra_cruceros.set_index("cruise_id")
    
    self.assertEquals(indexado.loc[5823, "region"], "Nacional")     
    
  def test_cruceros_de_usa_son_nan(self):
    indexado = muestra_cruceros.set_index("cruise_id")
    
    self.assertTrue(pd.isna(indexado.loc[8829, "region"]))     
        
    