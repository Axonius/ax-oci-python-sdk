# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unique_key import UniqueKey
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrimaryKey(UniqueKey):
    """
    The primary key object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrimaryKey object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.PrimaryKey.model_type` attribute
        of this class is ``PRIMARY_KEY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this PrimaryKey.
            Allowed values for this property are: "PRIMARY_KEY", "UNIQUE_KEY"
        :type model_type: str

        :param key:
            The value to assign to the key property of this PrimaryKey.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PrimaryKey.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PrimaryKey.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this PrimaryKey.
        :type name: str

        :param attribute_refs:
            The value to assign to the attribute_refs property of this PrimaryKey.
        :type attribute_refs: list[oci.data_integration.models.KeyAttribute]

        :param object_status:
            The value to assign to the object_status property of this PrimaryKey.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'attribute_refs': 'list[KeyAttribute]',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'attribute_refs': 'attributeRefs',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._attribute_refs = None
        self._object_status = None
        self._model_type = 'PRIMARY_KEY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
