from pathlib import Path

import pytest

from bloom_filter import BloomFilter


class TestDomainsList:
    filter = BloomFilter.from_file(
        sorted(Path().glob("bloom_filter_*.json"), reverse=True)[0]
    )

    @pytest.mark.parametrize(
        "domain_to_test",
        [
            l.strip()
            for l in sorted(Path().glob("domains_in_filter_*.txt"), reverse=True)[0]
            .read_text()
            .splitlines()
        ],
    )
    def test_domain_in_list(self, domain_to_test):
        assert self.filter.might_contain(domain_to_test)
