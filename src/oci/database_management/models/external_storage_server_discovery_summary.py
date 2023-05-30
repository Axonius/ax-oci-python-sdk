# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity_discovered import EntityDiscovered
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalStorageServerDiscoverySummary(EntityDiscovered):
    """
    The Exadata storage server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalStorageServerDiscoverySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalStorageServerDiscoverySummary.entity_type` attribute
        of this class is ``STORAGE_SERVER_DISCOVER_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalStorageServerDiscoverySummary.
        :type id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalStorageServerDiscoverySummary.
        :type agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this ExternalStorageServerDiscoverySummary.
        :type connector_id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalStorageServerDiscoverySummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalStorageServerDiscoverySummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalStorageServerDiscoverySummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalStorageServerDiscoverySummary.
        :type status: str

        :param discover_status:
            The value to assign to the discover_status property of this ExternalStorageServerDiscoverySummary.
            Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING"
        :type discover_status: str

        :param discover_error_code:
            The value to assign to the discover_error_code property of this ExternalStorageServerDiscoverySummary.
        :type discover_error_code: str

        :param discover_error_msg:
            The value to assign to the discover_error_msg property of this ExternalStorageServerDiscoverySummary.
        :type discover_error_msg: str

        :param entity_type:
            The value to assign to the entity_type property of this ExternalStorageServerDiscoverySummary.
            Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER"
        :type entity_type: str

        :param ip_address:
            The value to assign to the ip_address property of this ExternalStorageServerDiscoverySummary.
        :type ip_address: str

        :param make_model:
            The value to assign to the make_model property of this ExternalStorageServerDiscoverySummary.
        :type make_model: str

        :param cpu_count:
            The value to assign to the cpu_count property of this ExternalStorageServerDiscoverySummary.
        :type cpu_count: int

        :param memory_gb:
            The value to assign to the memory_gb property of this ExternalStorageServerDiscoverySummary.
        :type memory_gb: float

        :param connector_name:
            The value to assign to the connector_name property of this ExternalStorageServerDiscoverySummary.
        :type connector_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'agent_id': 'str',
            'connector_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'discover_status': 'str',
            'discover_error_code': 'str',
            'discover_error_msg': 'str',
            'entity_type': 'str',
            'ip_address': 'str',
            'make_model': 'str',
            'cpu_count': 'int',
            'memory_gb': 'float',
            'connector_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'agent_id': 'agentId',
            'connector_id': 'connectorId',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'discover_status': 'discoverStatus',
            'discover_error_code': 'discoverErrorCode',
            'discover_error_msg': 'discoverErrorMsg',
            'entity_type': 'entityType',
            'ip_address': 'ipAddress',
            'make_model': 'makeModel',
            'cpu_count': 'cpuCount',
            'memory_gb': 'memoryGB',
            'connector_name': 'connectorName'
        }

        self._id = None
        self._agent_id = None
        self._connector_id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._discover_status = None
        self._discover_error_code = None
        self._discover_error_msg = None
        self._entity_type = None
        self._ip_address = None
        self._make_model = None
        self._cpu_count = None
        self._memory_gb = None
        self._connector_name = None
        self._entity_type = 'STORAGE_SERVER_DISCOVER_SUMMARY'

    @property
    def ip_address(self):
        """
        Gets the ip_address of this ExternalStorageServerDiscoverySummary.
        The IP address of the storage server.


        :return: The ip_address of this ExternalStorageServerDiscoverySummary.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this ExternalStorageServerDiscoverySummary.
        The IP address of the storage server.


        :param ip_address: The ip_address of this ExternalStorageServerDiscoverySummary.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def make_model(self):
        """
        Gets the make_model of this ExternalStorageServerDiscoverySummary.
        The make model of the storage server.


        :return: The make_model of this ExternalStorageServerDiscoverySummary.
        :rtype: str
        """
        return self._make_model

    @make_model.setter
    def make_model(self, make_model):
        """
        Sets the make_model of this ExternalStorageServerDiscoverySummary.
        The make model of the storage server.


        :param make_model: The make_model of this ExternalStorageServerDiscoverySummary.
        :type: str
        """
        self._make_model = make_model

    @property
    def cpu_count(self):
        """
        Gets the cpu_count of this ExternalStorageServerDiscoverySummary.
        The cpu count of the storage server.


        :return: The cpu_count of this ExternalStorageServerDiscoverySummary.
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """
        Sets the cpu_count of this ExternalStorageServerDiscoverySummary.
        The cpu count of the storage server.


        :param cpu_count: The cpu_count of this ExternalStorageServerDiscoverySummary.
        :type: int
        """
        self._cpu_count = cpu_count

    @property
    def memory_gb(self):
        """
        Gets the memory_gb of this ExternalStorageServerDiscoverySummary.
        The memory size in GB of the storage server.


        :return: The memory_gb of this ExternalStorageServerDiscoverySummary.
        :rtype: float
        """
        return self._memory_gb

    @memory_gb.setter
    def memory_gb(self, memory_gb):
        """
        Sets the memory_gb of this ExternalStorageServerDiscoverySummary.
        The memory size in GB of the storage server.


        :param memory_gb: The memory_gb of this ExternalStorageServerDiscoverySummary.
        :type: float
        """
        self._memory_gb = memory_gb

    @property
    def connector_name(self):
        """
        Gets the connector_name of this ExternalStorageServerDiscoverySummary.
        The connector name of the storage server in rediscovery case.


        :return: The connector_name of this ExternalStorageServerDiscoverySummary.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this ExternalStorageServerDiscoverySummary.
        The connector name of the storage server in rediscovery case.


        :param connector_name: The connector_name of this ExternalStorageServerDiscoverySummary.
        :type: str
        """
        self._connector_name = connector_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other