#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Mailme API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Mailme API.
#
# Hive Mailme API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Mailme API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Mailme API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from typing import NotRequired, Sequence, TypedDict
from appier import API as BaseAPI

BASE_URL: str = ...

class Attachment(TypedDict):
    name: str
    data: str
    mime: str
    hash: str
    etag: str
    guid: str
    engine: str

class AttachmentPayload(TypedDict):
    name: str
    data: str
    mime: NotRequired[str]
    hash: NotRequired[str]
    etag: NotRequired[str]
    guid: NotRequired[str]
    engine: NotRequired[str]

class Message(TypedDict):
    sender: str | None
    receivers: Sequence[str]
    cc: Sequence[str]
    bcc: Sequence[str]
    reply_to: Sequence[str]
    subject: str
    title: str
    subtitle: str | None
    contents: str
    copyright: str
    logo_url: str | None
    attachments: Sequence[Attachment]
    id: str | None
    inline: bool
    style: str
    mode: str

class MessagePayload(TypedDict):
    receivers: Sequence[str]
    subject: NotRequired[str]
    title: NotRequired[str]
    contents: NotRequired[str]
    copyright: NotRequired[str]
    attachments: NotRequired[Sequence[AttachmentPayload]]
    inline: NotRequired[bool]
    style: NotRequired[str]
    mode: NotRequired[str]

class API(BaseAPI):
    def send(self, payload: MessagePayload) -> Message: ...
