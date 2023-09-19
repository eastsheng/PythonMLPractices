import pubchempy as pcp
from rdkit import Chem
# from rdkit.Chem import AllChem, Draw

class SearchCompounds(object):
	"""docstring for SearchCompounds"""
	def __init__(self, ):
		super(SearchCompounds, self).__init__()


	def get_mols_list(self,compounds):
		number_of_compounds = len(compounds)
		mols = []
		for i in range(number_of_compounds):
			mol = Chem.MolFromSmiles(compounds[i].canonical_smiles)
			mols.append(mol)

		return mols


	def get_smiles_list(self,compounds):
		number_of_compounds = len(compounds)
		smiles = []
		for i in range(number_of_compounds):
			smiles.append(compounds[i].canonical_smiles)

		return smiles		