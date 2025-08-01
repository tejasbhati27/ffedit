import os
from datetime import datetime
from typing import Optional

from ffedit.filesystem import get_file_extension, get_file_name


def get_step_output_path(job_id : str, step_index : int, output_path : str) -> Optional[str]:
	if output_path:
		output_directory_path, _ = os.path.split(output_path)
		output_file_name = get_file_name(_)
		output_file_extension = get_file_extension(_)
		return os.path.join(output_directory_path, output_file_name + '-' + job_id + '-' + str(step_index) + output_file_extension)
	return None


def suggest_job_id(job_prefix : str = 'job') -> str:
	return job_prefix + '-' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
