from rdkit import Chem
from rdkit.Chem import Draw
smi = 'CCCc1nn(C)c2C(=O)NC(=Nc12)c3cc(ccc3OCC)S(=O)(=O)N4CCN(C)CC4'
m = Chem.MolFromSmiles(smi)
Draw.MolToImageFile(m,"mol.jpg")