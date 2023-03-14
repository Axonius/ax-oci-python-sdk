# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_resource_statistics import HostResourceStatistics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostStorageStatistics(HostResourceStatistics):
    """
    Contains storage statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostStorageStatistics object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostStorageStatistics.resource_name` attribute
        of this class is ``HOST_STORAGE_STATISTICS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this HostStorageStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this HostStorageStatistics.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this HostStorageStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this HostStorageStatistics.
        :type usage_change_percent: float

        :param resource_name:
            The value to assign to the resource_name property of this HostStorageStatistics.
            Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS", "HOST_STORAGE_STATISTICS", "HOST_NETWORK_STATISTICS"
        :type resource_name: str

        :param filesystem_available_in_percent:
            The value to assign to the filesystem_available_in_percent property of this HostStorageStatistics.
        :type filesystem_available_in_percent: float

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'resource_name': 'str',
            'filesystem_available_in_percent': 'float'
        }

        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'resource_name': 'resourceName',
            'filesystem_available_in_percent': 'filesystemAvailableInPercent'
        }

        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._resource_name = None
        self._filesystem_available_in_percent = None
        self._resource_name = 'HOST_STORAGE_STATISTICS'

    @property
    def filesystem_available_in_percent(self):
        """
        Gets the filesystem_available_in_percent of this HostStorageStatistics.

        :return: The filesystem_available_in_percent of this HostStorageStatistics.
        :rtype: float
        """
        return self._filesystem_available_in_percent

    @filesystem_available_in_percent.setter
    def filesystem_available_in_percent(self, filesystem_available_in_percent):
        """
        Sets the filesystem_available_in_percent of this HostStorageStatistics.

        :param filesystem_available_in_percent: The filesystem_available_in_percent of this HostStorageStatistics.
        :type: float
        """
        self._filesystem_available_in_percent = filesystem_available_in_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other