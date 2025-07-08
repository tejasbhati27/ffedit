from typing import Optional

METADATA =\
{
	'name': 'ffedit',
	'description': 'Industry leading face manipulation platform',
	'version': '3.3.0',
	'license': 'OpenRAIL-AS',
	'author': 'Henry Ruhs',
	'url': 'https://ffedit.io'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
