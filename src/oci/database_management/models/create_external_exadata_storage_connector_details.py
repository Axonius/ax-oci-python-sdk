# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalExadataStorageConnectorDetails(object):
    """
    The details of creating the connector to the Exadata storage server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalExadataStorageConnectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_server_id:
            The value to assign to the storage_server_id property of this CreateExternalExadataStorageConnectorDetails.
        :type storage_server_id: str

        :param agent_id:
            The value to assign to the agent_id property of this CreateExternalExadataStorageConnectorDetails.
        :type agent_id: str

        :param connector_name:
            The value to assign to the connector_name property of this CreateExternalExadataStorageConnectorDetails.
        :type connector_name: str

        :param connection_uri:
            The value to assign to the connection_uri property of this CreateExternalExadataStorageConnectorDetails.
        :type connection_uri: str

        :param credential_info:
            The value to assign to the credential_info property of this CreateExternalExadataStorageConnectorDetails.
        :type credential_info: oci.database_management.models.RestCredential

        """
        self.swagger_types = {
            'storage_server_id': 'str',
            'agent_id': 'str',
            'connector_name': 'str',
            'connection_uri': 'str',
            'credential_info': 'RestCredential'
        }

        self.attribute_map = {
            'storage_server_id': 'storageServerId',
            'agent_id': 'agentId',
            'connector_name': 'connectorName',
            'connection_uri': 'connectionUri',
            'credential_info': 'credentialInfo'
        }

        self._storage_server_id = None
        self._agent_id = None
        self._connector_name = None
        self._connection_uri = None
        self._credential_info = None

    @property
    def storage_server_id(self):
        """
        **[Required]** Gets the storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._storage_server_id

    @storage_server_id.setter
    def storage_server_id(self, storage_server_id):
        """
        Sets the storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param storage_server_id: The storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._storage_server_id = storage_server_id

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connector_name(self):
        """
        **[Required]** Gets the connector_name of this CreateExternalExadataStorageConnectorDetails.
        The connector name if OCI connector is created.


        :return: The connector_name of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this CreateExternalExadataStorageConnectorDetails.
        The connector name if OCI connector is created.


        :param connector_name: The connector_name of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connector_name = connector_name

    @property
    def connection_uri(self):
        """
        **[Required]** Gets the connection_uri of this CreateExternalExadataStorageConnectorDetails.
        The unique connection string of the connection. For example, \"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\".


        :return: The connection_uri of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """
        Sets the connection_uri of this CreateExternalExadataStorageConnectorDetails.
        The unique connection string of the connection. For example, \"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\".


        :param connection_uri: The connection_uri of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connection_uri = connection_uri

    @property
    def credential_info(self):
        """
        **[Required]** Gets the credential_info of this CreateExternalExadataStorageConnectorDetails.

        :return: The credential_info of this CreateExternalExadataStorageConnectorDetails.
        :rtype: oci.database_management.models.RestCredential
        """
        return self._credential_info

    @credential_info.setter
    def credential_info(self, credential_info):
        """
        Sets the credential_info of this CreateExternalExadataStorageConnectorDetails.

        :param credential_info: The credential_info of this CreateExternalExadataStorageConnectorDetails.
        :type: oci.database_management.models.RestCredential
        """
        self._credential_info = credential_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other