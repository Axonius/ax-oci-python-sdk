# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrSourceSummary(object):
    """
    Summary of an AwrSource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param awr_hub_id:
            The value to assign to the awr_hub_id property of this AwrSourceSummary.
        :type awr_hub_id: str

        :param name:
            The value to assign to the name property of this AwrSourceSummary.
        :type name: str

        :param awr_source_database_id:
            The value to assign to the awr_source_database_id property of this AwrSourceSummary.
        :type awr_source_database_id: str

        :param snapshots_uploaded:
            The value to assign to the snapshots_uploaded property of this AwrSourceSummary.
        :type snapshots_uploaded: float

        :param min_snapshot_identifier:
            The value to assign to the min_snapshot_identifier property of this AwrSourceSummary.
        :type min_snapshot_identifier: float

        :param max_snapshot_identifier:
            The value to assign to the max_snapshot_identifier property of this AwrSourceSummary.
        :type max_snapshot_identifier: float

        :param time_first_snapshot_generated:
            The value to assign to the time_first_snapshot_generated property of this AwrSourceSummary.
        :type time_first_snapshot_generated: datetime

        :param time_last_snapshot_generated:
            The value to assign to the time_last_snapshot_generated property of this AwrSourceSummary.
        :type time_last_snapshot_generated: datetime

        :param hours_since_last_import:
            The value to assign to the hours_since_last_import property of this AwrSourceSummary.
        :type hours_since_last_import: float

        """
        self.swagger_types = {
            'awr_hub_id': 'str',
            'name': 'str',
            'awr_source_database_id': 'str',
            'snapshots_uploaded': 'float',
            'min_snapshot_identifier': 'float',
            'max_snapshot_identifier': 'float',
            'time_first_snapshot_generated': 'datetime',
            'time_last_snapshot_generated': 'datetime',
            'hours_since_last_import': 'float'
        }

        self.attribute_map = {
            'awr_hub_id': 'awrHubId',
            'name': 'name',
            'awr_source_database_id': 'awrSourceDatabaseId',
            'snapshots_uploaded': 'snapshotsUploaded',
            'min_snapshot_identifier': 'minSnapshotIdentifier',
            'max_snapshot_identifier': 'maxSnapshotIdentifier',
            'time_first_snapshot_generated': 'timeFirstSnapshotGenerated',
            'time_last_snapshot_generated': 'timeLastSnapshotGenerated',
            'hours_since_last_import': 'hoursSinceLastImport'
        }

        self._awr_hub_id = None
        self._name = None
        self._awr_source_database_id = None
        self._snapshots_uploaded = None
        self._min_snapshot_identifier = None
        self._max_snapshot_identifier = None
        self._time_first_snapshot_generated = None
        self._time_last_snapshot_generated = None
        self._hours_since_last_import = None

    @property
    def awr_hub_id(self):
        """
        **[Required]** Gets the awr_hub_id of this AwrSourceSummary.
        AWR Hub OCID


        :return: The awr_hub_id of this AwrSourceSummary.
        :rtype: str
        """
        return self._awr_hub_id

    @awr_hub_id.setter
    def awr_hub_id(self, awr_hub_id):
        """
        Sets the awr_hub_id of this AwrSourceSummary.
        AWR Hub OCID


        :param awr_hub_id: The awr_hub_id of this AwrSourceSummary.
        :type: str
        """
        self._awr_hub_id = awr_hub_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrSourceSummary.
        Database name of the Source database for which AWR Data will be uploaded to AWR Hub.


        :return: The name of this AwrSourceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrSourceSummary.
        Database name of the Source database for which AWR Data will be uploaded to AWR Hub.


        :param name: The name of this AwrSourceSummary.
        :type: str
        """
        self._name = name

    @property
    def awr_source_database_id(self):
        """
        **[Required]** Gets the awr_source_database_id of this AwrSourceSummary.
        DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.


        :return: The awr_source_database_id of this AwrSourceSummary.
        :rtype: str
        """
        return self._awr_source_database_id

    @awr_source_database_id.setter
    def awr_source_database_id(self, awr_source_database_id):
        """
        Sets the awr_source_database_id of this AwrSourceSummary.
        DatabaseId of the Source database for which AWR Data will be uploaded to AWR Hub.


        :param awr_source_database_id: The awr_source_database_id of this AwrSourceSummary.
        :type: str
        """
        self._awr_source_database_id = awr_source_database_id

    @property
    def snapshots_uploaded(self):
        """
        **[Required]** Gets the snapshots_uploaded of this AwrSourceSummary.
        Number of AWR snapshots uploaded from the Source database.


        :return: The snapshots_uploaded of this AwrSourceSummary.
        :rtype: float
        """
        return self._snapshots_uploaded

    @snapshots_uploaded.setter
    def snapshots_uploaded(self, snapshots_uploaded):
        """
        Sets the snapshots_uploaded of this AwrSourceSummary.
        Number of AWR snapshots uploaded from the Source database.


        :param snapshots_uploaded: The snapshots_uploaded of this AwrSourceSummary.
        :type: float
        """
        self._snapshots_uploaded = snapshots_uploaded

    @property
    def min_snapshot_identifier(self):
        """
        **[Required]** Gets the min_snapshot_identifier of this AwrSourceSummary.
        The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :return: The min_snapshot_identifier of this AwrSourceSummary.
        :rtype: float
        """
        return self._min_snapshot_identifier

    @min_snapshot_identifier.setter
    def min_snapshot_identifier(self, min_snapshot_identifier):
        """
        Sets the min_snapshot_identifier of this AwrSourceSummary.
        The minimum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :param min_snapshot_identifier: The min_snapshot_identifier of this AwrSourceSummary.
        :type: float
        """
        self._min_snapshot_identifier = min_snapshot_identifier

    @property
    def max_snapshot_identifier(self):
        """
        **[Required]** Gets the max_snapshot_identifier of this AwrSourceSummary.
        The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :return: The max_snapshot_identifier of this AwrSourceSummary.
        :rtype: float
        """
        return self._max_snapshot_identifier

    @max_snapshot_identifier.setter
    def max_snapshot_identifier(self, max_snapshot_identifier):
        """
        Sets the max_snapshot_identifier of this AwrSourceSummary.
        The maximum snapshot identifier of the source database for which AWR data is uploaded to AWR Hub.


        :param max_snapshot_identifier: The max_snapshot_identifier of this AwrSourceSummary.
        :type: float
        """
        self._max_snapshot_identifier = max_snapshot_identifier

    @property
    def time_first_snapshot_generated(self):
        """
        **[Required]** Gets the time_first_snapshot_generated of this AwrSourceSummary.
        The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :return: The time_first_snapshot_generated of this AwrSourceSummary.
        :rtype: datetime
        """
        return self._time_first_snapshot_generated

    @time_first_snapshot_generated.setter
    def time_first_snapshot_generated(self, time_first_snapshot_generated):
        """
        Sets the time_first_snapshot_generated of this AwrSourceSummary.
        The time at which the earliest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :param time_first_snapshot_generated: The time_first_snapshot_generated of this AwrSourceSummary.
        :type: datetime
        """
        self._time_first_snapshot_generated = time_first_snapshot_generated

    @property
    def time_last_snapshot_generated(self):
        """
        **[Required]** Gets the time_last_snapshot_generated of this AwrSourceSummary.
        The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :return: The time_last_snapshot_generated of this AwrSourceSummary.
        :rtype: datetime
        """
        return self._time_last_snapshot_generated

    @time_last_snapshot_generated.setter
    def time_last_snapshot_generated(self, time_last_snapshot_generated):
        """
        Sets the time_last_snapshot_generated of this AwrSourceSummary.
        The time at which the latest snapshot was generated in the source database for which data is uploaded to AWR Hub. An RFC3339 formatted datetime string


        :param time_last_snapshot_generated: The time_last_snapshot_generated of this AwrSourceSummary.
        :type: datetime
        """
        self._time_last_snapshot_generated = time_last_snapshot_generated

    @property
    def hours_since_last_import(self):
        """
        **[Required]** Gets the hours_since_last_import of this AwrSourceSummary.
        Number of hours since last AWR snapshots import happened from the Source database.


        :return: The hours_since_last_import of this AwrSourceSummary.
        :rtype: float
        """
        return self._hours_since_last_import

    @hours_since_last_import.setter
    def hours_since_last_import(self, hours_since_last_import):
        """
        Sets the hours_since_last_import of this AwrSourceSummary.
        Number of hours since last AWR snapshots import happened from the Source database.


        :param hours_since_last_import: The hours_since_last_import of this AwrSourceSummary.
        :type: float
        """
        self._hours_since_last_import = hours_since_last_import

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
