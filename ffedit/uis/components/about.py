import random
from typing import Optional

import gradio

from ffedit import metadata, wording

METADATA_BUTTON : Optional[gradio.Button] = None
ACTION_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global METADATA_BUTTON
	global ACTION_BUTTON

	action = random.choice(
	[
		{
			'wording': wording.get('about.become_a_member'),
			'url': 'https://subscribe.ffedit.io'
		},
		{
			'wording': wording.get('about.join_our_community'),
			'url': 'https://join.ffedit.io'
		},
		{
			'wording': wording.get('about.read_the_documentation'),
			'url': 'https://docs.ffedit.io'
		}
	])

	METADATA_BUTTON = gradio.Button(
		value = metadata.get('name') + ' ' + metadata.get('version'),
		variant = 'primary',
		link = metadata.get('url')
	)
	ACTION_BUTTON = gradio.Button(
		value = action.get('wording'),
		link = action.get('url'),
		size = 'sm'
	)
