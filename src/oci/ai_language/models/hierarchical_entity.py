# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HierarchicalEntity(object):
    """
    Hierarchical entity object
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HierarchicalEntity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param offset:
            The value to assign to the offset property of this HierarchicalEntity.
        :type offset: int

        :param length:
            The value to assign to the length property of this HierarchicalEntity.
        :type length: int

        :param text:
            The value to assign to the text property of this HierarchicalEntity.
        :type text: str

        :param type:
            The value to assign to the type property of this HierarchicalEntity.
        :type type: str

        :param sub_type:
            The value to assign to the sub_type property of this HierarchicalEntity.
        :type sub_type: str

        :param score:
            The value to assign to the score property of this HierarchicalEntity.
        :type score: float

        """
        self.swagger_types = {
            'offset': 'int',
            'length': 'int',
            'text': 'str',
            'type': 'str',
            'sub_type': 'str',
            'score': 'float'
        }

        self.attribute_map = {
            'offset': 'offset',
            'length': 'length',
            'text': 'text',
            'type': 'type',
            'sub_type': 'subType',
            'score': 'score'
        }

        self._offset = None
        self._length = None
        self._text = None
        self._type = None
        self._sub_type = None
        self._score = None

    @property
    def offset(self):
        """
        Gets the offset of this HierarchicalEntity.
        The number of Unicode code points preceding this entity in the submitted text.


        :return: The offset of this HierarchicalEntity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this HierarchicalEntity.
        The number of Unicode code points preceding this entity in the submitted text.


        :param offset: The offset of this HierarchicalEntity.
        :type: int
        """
        self._offset = offset

    @property
    def length(self):
        """
        Gets the length of this HierarchicalEntity.
        Length of entity text


        :return: The length of this HierarchicalEntity.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this HierarchicalEntity.
        Length of entity text


        :param length: The length of this HierarchicalEntity.
        :type: int
        """
        self._length = length

    @property
    def text(self):
        """
        Gets the text of this HierarchicalEntity.
        Entity text like name of person, location, and so on.


        :return: The text of this HierarchicalEntity.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this HierarchicalEntity.
        Entity text like name of person, location, and so on.


        :param text: The text of this HierarchicalEntity.
        :type: str
        """
        self._text = text

    @property
    def type(self):
        """
        Gets the type of this HierarchicalEntity.
        Type of entity text like PER, LOC.


        :return: The type of this HierarchicalEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HierarchicalEntity.
        Type of entity text like PER, LOC.


        :param type: The type of this HierarchicalEntity.
        :type: str
        """
        self._type = type

    @property
    def sub_type(self):
        """
        Gets the sub_type of this HierarchicalEntity.
        Sub-type of entity text like GPE for LOCATION type


        :return: The sub_type of this HierarchicalEntity.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this HierarchicalEntity.
        Sub-type of entity text like GPE for LOCATION type


        :param sub_type: The sub_type of this HierarchicalEntity.
        :type: str
        """
        self._sub_type = sub_type

    @property
    def score(self):
        """
        Gets the score of this HierarchicalEntity.
        Score or confidence for detected entity.


        :return: The score of this HierarchicalEntity.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this HierarchicalEntity.
        Score or confidence for detected entity.


        :param score: The score of this HierarchicalEntity.
        :type: float
        """
        self._score = score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
