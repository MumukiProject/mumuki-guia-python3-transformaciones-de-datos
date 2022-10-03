class Test(unittest.TestCase):
  def setUp(self):
    self.cruceros = cruceros.set_index("cruise_id")
  
  def test_nacionales(self):
    self.assertEquals(self.cruceros.loc[1]["region"], "Nacional", "El crucero 1 debería tener región nacional")
    self.assertEquals(self.cruceros.loc[1]["region"], "Nacional", "El crucero 1 debería tener región nacional")
  
  
  def test_regionales(self):
    self.assertEquals(self.cruceros.loc[1]["region"], "Regional", "El crucero 1 debería tener región regional")
    self.assertEquals(self.cruceros.loc[1]["region"], "Regional", "El crucero 1 debería tener región regional")  
  
  def test_no_regionales(self):
    self.assertEquals(self.cruceros.loc[1]["region"], "No regional", "El crucero 1 debería tener región no regional")
    self.assertEquals(self.cruceros.loc[1]["region"], "No regional", "El crucero 1 debería tener región no regional")