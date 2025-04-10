# -*- coding: utf-8 -*-

from collections import OrderedDict
from typing import List
from torch.utils.data import Dataset as TorchDataset

class MathEntityType:
    def __init__(self, identifier, index, name, description):
        self._identifier = identifier
        self._index = index
        self._name = name
        self._description = description

    @property
    def identifier(self):
        return self._identifier

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def __int__(self):
        return self._index

    def __eq__(self, other):
        if isinstance(other, MathEntityType):
            return self._identifier == other._identifier
        return False

    def __hash__(self):
        return hash(self._identifier)

class MathToken:
    def __init__(self, tid: int, index: int, span_start: int, span_end: int, phrase: str):
        self._tid = tid  # ID within the corresponding dataset
        self._index = index  # original token index in document

        self._span_start = span_start  # start of token span in document (inclusive)
        self._span_end = span_end  # end of token span in document (exclusive)
        self._phrase = phrase

    @property
    def index(self):
        return self._index

    @property
    def span_start(self):
        return self._span_start

    @property
    def span_end(self):
        return self._span_end

    @property
    def span(self):
        return self._span_start, self._span_end

    @property
    def phrase(self):
        return self._phrase

    def __eq__(self, other):
        if isinstance(other, MathToken):
            return self._tid == other._tid
        return False

    def __hash__(self):
        return hash(self._tid)

    def __str__(self):
        return self._phrase

    def __repr__(self):
        return self._phrase

class TokenSpan:
    def __init__(self, tokens):
        self._tokens = tokens

    @property
    def span_start(self):
        return self._tokens[0].span_start

    @property
    def span_end(self):
        return self._tokens[-1].span_end

    @property
    def span(self):
        return self.span_start, self.span_end

    def __getitem__(self, s):
        if isinstance(s, slice):
            return TokenSpan(self._tokens[s.start:s.stop:s.step])
        else:
            return self._tokens[s]

    def __iter__(self):
        return iter(self._tokens)

    def __len__(self):
        return len(self._tokens)

class MathEntity:
    def __init__(self, eid: int, entity_type: MathEntityType, tokens: List[MathToken], phrase: str):
        self._eid = eid  # ID within the corresponding dataset
        self._entity_type = entity_type
        self._tokens = tokens
        self._phrase = phrase

    def as_tuple(self):
        return self.span_start, self.span_end, self._entity_type

    @property
    def entity_type(self):
        return self._entity_type

    @property
    def tokens(self):
        return TokenSpan(self._tokens)

    @property
    def span_start(self):
        return self._tokens[0].span_start

    @property
    def span_end(self):
        return self._tokens[-1].span_end

    @property
    def span(self):
        return self.span_start, self.span_end

    @property
    def phrase(self):
        return self._phrase

    def __eq__(self, other):
        if isinstance(other, MathEntity):
            return self._eid == other._eid
        return False

    def __hash__(self):
        return hash(self._eid)

    def __str__(self):
        return self._phrase

class MathDocument:
    def __init__(self, doc_id: int, tokens: List[MathToken], entities: List[MathEntity]):
        self._doc_id = doc_id
        self._tokens = tokens
        self._entities = entities

    @property
    def doc_id(self):
        return self._doc_id

    @property
    def tokens(self):
        return self._tokens

    @property
    def entities(self):
        return self._entities
