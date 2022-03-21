import { useState } from "react";

const useApi = (apiFunc: any) => {
  const [data, setData]: any = useState(null);
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  const [message, setMessage]: any = useState(null);
  const [status, setStatus] = useState(null);

  const resetState = () => {
    setError(false);
    setMessage(null);
  };

  // class Private {
  //   _setError(bool: boolean) {
  //     setError(bool);
  //     return this;
  //   }

  //   _setMessage(str: string) {
  //     setMessage(str);
  //     return this;
  //   }

  //   _setLoading(bool: boolean) {
  //     setLoading(bool);
  //     return this;
  //   }

  //   _reset() {
  //     resetState();
  //   }
  // }

  const request = async (...args: any) => {
    resetState();
    setLoading(true);
    const response = await apiFunc(...args);
    setLoading(false);

    setStatus(response.status);

    if (!response.ok) {
      if (response.data) {
        setError(true);
        return setMessage(response.data.message);
      }
      setMessage("An unexpected error ocurred. Try again later");
      return setError(true);
    }

    setError(false);
    setMessage(response.data.message);
    setData(response.data);
    return response;
  };

  return {
    data,
    message,
    error,
    loading,
    status,
    request,
    // _private: new Private(),
  };
};

export default useApi;
