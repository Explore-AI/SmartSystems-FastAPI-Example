import { get, size } from "lodash";
import {
  handleJsonResponse,
  handleRequestHeaders,
  getAbsURL,
} from "../common/utils";

/* to get regions*/
export const getUsers = async () => {
  const requestOptions = await handleRequestHeaders();
  const url = getAbsURL("users/");
  return fetch(url, requestOptions)
    .then(handleJsonResponse)
    .then((data) => {
      return data;
    });
};

export const updateUser = async (data) => {
  const headerOptions = await handleRequestHeaders("PUT");
  const requestOptions = {
    ...headerOptions,
    headers: {
      ...headerOptions.headers,
      "Content-Type": "application/json",
      // "Content-Length": Buffer.byteLength(data),
      "Content-Length": size(JSON.stringify(data)),
    },
    body: JSON.stringify(data),
  };
  let url = "users/" + get(data, "Id");
  return fetch(getAbsURL(url), requestOptions)
    .then(handleJsonResponse)
    .then((data) => {
      return data;
    });
};
