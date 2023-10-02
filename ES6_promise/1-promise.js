export default function getFullResponseFromAPI(success) {
    const prom = new Promise(
        (success) => { return { status: 200, body: 'Success' } },
        console.error("The fake API is not working currently")
    );
    return prom;
};
