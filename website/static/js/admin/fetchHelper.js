window.addEventListener("DOMContentLoaded", () => {
    // vars
    const button1 = document.getElementById(fetchState[0].id)
    const button2 = document.getElementById(fetchState[1].id)
    const fieldForm = document.querySelector(`.content`)

    // methods
    const getCallout = (text, type) => {
        const callout = document.createElement('div') 
        callout.classList.add('callout', `callout-${type}`)
        callout.innerHTML = text
        return callout
    }
    
    const showCallout = (text, type='danger') => {
        const callout = getCallout(text, type)
        fieldForm.insertBefore(callout, fieldForm.children[0])
    }

    function accept_transaction(url, status) {
        return fetch(`${url}?status=${status}&t=${new Date().getTime()}`, {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            method: "GET",
            mode: 'same-origin'
        }).then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error('Something went wrong');
        }).then(data => {
            return data
        });
    }

    function download_transaction(url) {
        return fetch(`${url}?t=${new Date().getTime()}`)
        .then(response => {
            response.blob().then(blob => {
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = "transactions.zip"; // Set the desired file name

                link.click();

                link.remove();
                URL.revokeObjectURL(url);
              })
         })
    }

    // events
    if (button1)
        button1.addEventListener("click", async (event) => {
            event.preventDefault();
            button1.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Ожидайте`
            const response = await accept_transaction(fetchState[0].url, 5)

            if (response.total_amount) {
                showCallout(`Транзакции выгруженны кол.во.: ${response.amount} сумма: ${response.total_amount}`, "success")
            } else {
                showCallout(`Транзакции не найдены`)
            }
            button1.innerHTML = "Получить транзакции"
        })

    if (button2)
        button2.addEventListener("click", async (event) => {
            event.preventDefault();
            button2.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Ожидайте`
            await download_transaction(fetchState[1].url)
            const response = await accept_transaction(fetchState[0].url, 4)
            if (response.total_amount) {
                showCallout(`Транзакции обновлены кол.во.: ${response.amount} сумма: ${response.total_amount}`, "success")
            } else {
                showCallout(`Транзакции не найдены`)
            }
            button2.innerHTML = "Подтвердить транзакции"
        })
})