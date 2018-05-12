#!/usr/bin/env python3

#usage:
#enter anaconda prompt
#go in the right folder 
#py.test

from as4_rv import count_kmers
import pytest

#avoid repetition by loading data in advance
@pytest.fixture
seq=Seq("ATTTGGATT")
	
def test_count_kmers():
	k=2
	counter=count_kmers(seq)
	assert len(counter)==5
	
#test k = 0 produces 0 kmers
def test_count_kmers0():
	k=0
	counter=count_kmers(seq)
	assert len(counter)==0

#test k = 1000 produces 0
def test_count_kmers1000():
	k=1000
	counter=count_kmers(seq)
	assert len(counter)==0

#test k = -2 produces 0
def test_count_kmers_neg():
	k=-2
	counter=count_kmers(seq)
	assert len(counter)==0
	
#test k = .3 produces 0
def test_count_kmers_dec():
	k=0.3
	counter=count_kmers(seq)
	assert len(counter)==0