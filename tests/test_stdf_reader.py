import os
import stdf
from tempfile import TemporaryFile
from unittest import TestCase


class TestStdfRecord(TestCase):
    def setUp(self) -> None:
        self.f = os.path.abspath(os.path.join(__file__, os.pardir, "data", "lot3.stdf.gz"))

    def test_stdf_record_open_file(self):
        with TemporaryFile() as f_out:
            stdf.StdfReader(self.f).export_csv(f_out)