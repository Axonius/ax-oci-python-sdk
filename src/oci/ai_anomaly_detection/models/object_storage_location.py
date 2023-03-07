# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .output_job_details import OutputJobDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageLocation(OutputJobDetails):
    """
    This is the specialised JSON format with an additional field for 'locationType'. This is a required field
    used for deciding if it is an object-storage location.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageLocation object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.ObjectStorageLocation.output_type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this ObjectStorageLocation.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type output_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectStorageLocation.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageLocation.
        :type bucket_name: str

        :param prefix:
            The value to assign to the prefix property of this ObjectStorageLocation.
        :type prefix: str

        """
        self.swagger_types = {
            'output_type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'prefix': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'prefix': 'prefix'
        }

        self._output_type = None
        self._namespace_name = None
        self._bucket_name = None
        self._prefix = None
        self._output_type = 'OBJECT_STORAGE'

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ObjectStorageLocation.
        Object Storage namespace.


        :return: The namespace_name of this ObjectStorageLocation.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectStorageLocation.
        Object Storage namespace.


        :param namespace_name: The namespace_name of this ObjectStorageLocation.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageLocation.
        Object Storage bucket name.


        :return: The bucket_name of this ObjectStorageLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageLocation.
        Object Storage bucket name.


        :param bucket_name: The bucket_name of this ObjectStorageLocation.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        """
        **[Required]** Gets the prefix of this ObjectStorageLocation.
        Object Storage folder name.


        :return: The prefix of this ObjectStorageLocation.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this ObjectStorageLocation.
        Object Storage folder name.


        :param prefix: The prefix of this ObjectStorageLocation.
        :type: str
        """
        self._prefix = prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other