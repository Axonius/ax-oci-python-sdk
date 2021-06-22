# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_option import ConnectionOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpoint(ConnectionOption):
    """
    The details required to establish a connection to the database using a private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.PrivateEndpoint.connection_type` attribute
        of this class is ``PRIVATE_ENDPOINT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this PrivateEndpoint.
            Allowed values for this property are: "PRIVATE_ENDPOINT", "ONPREM_CONNECTOR"
        :type connection_type: str

        :param datasafe_private_endpoint_id:
            The value to assign to the datasafe_private_endpoint_id property of this PrivateEndpoint.
        :type datasafe_private_endpoint_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'datasafe_private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'datasafe_private_endpoint_id': 'datasafePrivateEndpointId'
        }

        self._connection_type = None
        self._datasafe_private_endpoint_id = None
        self._connection_type = 'PRIVATE_ENDPOINT'

    @property
    def datasafe_private_endpoint_id(self):
        """
        Gets the datasafe_private_endpoint_id of this PrivateEndpoint.
        The OCID of the Data Safe private endpoint.


        :return: The datasafe_private_endpoint_id of this PrivateEndpoint.
        :rtype: str
        """
        return self._datasafe_private_endpoint_id

    @datasafe_private_endpoint_id.setter
    def datasafe_private_endpoint_id(self, datasafe_private_endpoint_id):
        """
        Sets the datasafe_private_endpoint_id of this PrivateEndpoint.
        The OCID of the Data Safe private endpoint.


        :param datasafe_private_endpoint_id: The datasafe_private_endpoint_id of this PrivateEndpoint.
        :type: str
        """
        self._datasafe_private_endpoint_id = datasafe_private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other