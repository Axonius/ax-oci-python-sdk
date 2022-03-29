# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallationSiteSummary(object):
    """
    Installation site of a Java Runtime.
    An installation site is a Java Runtime installed at a specific path on a managed instance.
    """

    #: A constant which can be used with the security_status property of a InstallationSiteSummary.
    #: This constant has a value of "UNKNOWN"
    SECURITY_STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the security_status property of a InstallationSiteSummary.
    #: This constant has a value of "UP_TO_DATE"
    SECURITY_STATUS_UP_TO_DATE = "UP_TO_DATE"

    #: A constant which can be used with the security_status property of a InstallationSiteSummary.
    #: This constant has a value of "UPDATE_REQUIRED"
    SECURITY_STATUS_UPDATE_REQUIRED = "UPDATE_REQUIRED"

    #: A constant which can be used with the security_status property of a InstallationSiteSummary.
    #: This constant has a value of "UPGRADE_REQUIRED"
    SECURITY_STATUS_UPGRADE_REQUIRED = "UPGRADE_REQUIRED"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a InstallationSiteSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new InstallationSiteSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param installation_key:
            The value to assign to the installation_key property of this InstallationSiteSummary.
        :type installation_key: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this InstallationSiteSummary.
        :type managed_instance_id: str

        :param jre:
            The value to assign to the jre property of this InstallationSiteSummary.
        :type jre: oci.jms.models.JavaRuntimeId

        :param security_status:
            The value to assign to the security_status property of this InstallationSiteSummary.
            Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type security_status: str

        :param path:
            The value to assign to the path property of this InstallationSiteSummary.
        :type path: str

        :param operating_system:
            The value to assign to the operating_system property of this InstallationSiteSummary.
        :type operating_system: oci.jms.models.OperatingSystem

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this InstallationSiteSummary.
        :type approximate_application_count: int

        :param time_last_seen:
            The value to assign to the time_last_seen property of this InstallationSiteSummary.
        :type time_last_seen: datetime

        :param blocklist:
            The value to assign to the blocklist property of this InstallationSiteSummary.
        :type blocklist: list[oci.jms.models.BlocklistEntry]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstallationSiteSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'installation_key': 'str',
            'managed_instance_id': 'str',
            'jre': 'JavaRuntimeId',
            'security_status': 'str',
            'path': 'str',
            'operating_system': 'OperatingSystem',
            'approximate_application_count': 'int',
            'time_last_seen': 'datetime',
            'blocklist': 'list[BlocklistEntry]',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'installation_key': 'installationKey',
            'managed_instance_id': 'managedInstanceId',
            'jre': 'jre',
            'security_status': 'securityStatus',
            'path': 'path',
            'operating_system': 'operatingSystem',
            'approximate_application_count': 'approximateApplicationCount',
            'time_last_seen': 'timeLastSeen',
            'blocklist': 'blocklist',
            'lifecycle_state': 'lifecycleState'
        }

        self._installation_key = None
        self._managed_instance_id = None
        self._jre = None
        self._security_status = None
        self._path = None
        self._operating_system = None
        self._approximate_application_count = None
        self._time_last_seen = None
        self._blocklist = None
        self._lifecycle_state = None

    @property
    def installation_key(self):
        """
        **[Required]** Gets the installation_key of this InstallationSiteSummary.
        The unique identifier for the installation of Java Runtime at a specific path on a specific operating system.


        :return: The installation_key of this InstallationSiteSummary.
        :rtype: str
        """
        return self._installation_key

    @installation_key.setter
    def installation_key(self, installation_key):
        """
        Sets the installation_key of this InstallationSiteSummary.
        The unique identifier for the installation of Java Runtime at a specific path on a specific operating system.


        :param installation_key: The installation_key of this InstallationSiteSummary.
        :type: str
        """
        self._installation_key = installation_key

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this InstallationSiteSummary.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this InstallationSiteSummary.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this InstallationSiteSummary.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this InstallationSiteSummary.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def jre(self):
        """
        Gets the jre of this InstallationSiteSummary.

        :return: The jre of this InstallationSiteSummary.
        :rtype: oci.jms.models.JavaRuntimeId
        """
        return self._jre

    @jre.setter
    def jre(self, jre):
        """
        Sets the jre of this InstallationSiteSummary.

        :param jre: The jre of this InstallationSiteSummary.
        :type: oci.jms.models.JavaRuntimeId
        """
        self._jre = jre

    @property
    def security_status(self):
        """
        Gets the security_status of this InstallationSiteSummary.
        The security status of the Java Runtime.

        Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The security_status of this InstallationSiteSummary.
        :rtype: str
        """
        return self._security_status

    @security_status.setter
    def security_status(self, security_status):
        """
        Sets the security_status of this InstallationSiteSummary.
        The security status of the Java Runtime.


        :param security_status: The security_status of this InstallationSiteSummary.
        :type: str
        """
        allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
        if not value_allowed_none_or_none_sentinel(security_status, allowed_values):
            security_status = 'UNKNOWN_ENUM_VALUE'
        self._security_status = security_status

    @property
    def path(self):
        """
        Gets the path of this InstallationSiteSummary.
        The file system path of the installation.


        :return: The path of this InstallationSiteSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this InstallationSiteSummary.
        The file system path of the installation.


        :param path: The path of this InstallationSiteSummary.
        :type: str
        """
        self._path = path

    @property
    def operating_system(self):
        """
        Gets the operating_system of this InstallationSiteSummary.

        :return: The operating_system of this InstallationSiteSummary.
        :rtype: oci.jms.models.OperatingSystem
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this InstallationSiteSummary.

        :param operating_system: The operating_system of this InstallationSiteSummary.
        :type: oci.jms.models.OperatingSystem
        """
        self._operating_system = operating_system

    @property
    def approximate_application_count(self):
        """
        Gets the approximate_application_count of this InstallationSiteSummary.
        The approximate count of applications running on this installation


        :return: The approximate_application_count of this InstallationSiteSummary.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this InstallationSiteSummary.
        The approximate count of applications running on this installation


        :param approximate_application_count: The approximate_application_count of this InstallationSiteSummary.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this InstallationSiteSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this InstallationSiteSummary.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this InstallationSiteSummary.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this InstallationSiteSummary.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    @property
    def blocklist(self):
        """
        Gets the blocklist of this InstallationSiteSummary.
        The list of operations that are blocklisted.


        :return: The blocklist of this InstallationSiteSummary.
        :rtype: list[oci.jms.models.BlocklistEntry]
        """
        return self._blocklist

    @blocklist.setter
    def blocklist(self, blocklist):
        """
        Sets the blocklist of this InstallationSiteSummary.
        The list of operations that are blocklisted.


        :param blocklist: The blocklist of this InstallationSiteSummary.
        :type: list[oci.jms.models.BlocklistEntry]
        """
        self._blocklist = blocklist

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this InstallationSiteSummary.
        The lifecycle state of the installation site.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstallationSiteSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstallationSiteSummary.
        The lifecycle state of the installation site.


        :param lifecycle_state: The lifecycle_state of this InstallationSiteSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
