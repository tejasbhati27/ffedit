import os

import pytest

from ffedit.jobs.job_helper import get_step_output_path


def test_get_step_output_path() -> None:
	assert get_step_output_path('test-job', 0, 'test.mp4') == 'test-test-job-0.mp4'
	assert get_step_output_path('test-job', 0, 'test/test.mp4') == os.path.join('test', 'test-test-job-0.mp4')
