class Test(unittest.TestCase):

  def test_cruceros_tiene_columna_sector_type(self):
    self.assertTrue("sector_type" in cruceros.columns)