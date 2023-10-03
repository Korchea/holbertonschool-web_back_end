export default function getFullResponseFromAPI(success) {
  let myPromise = new Promise(function (myResolve, myReject) {
    // "Producing Code" (May take some time)
    if (success === true) {
      myResolve({ status: 200, body: 'Success' }); // when successful
    }
    else {
      myReject(Error("The fake API is not working currently"));  // when error
    }
  });
  return myPromise;
};
