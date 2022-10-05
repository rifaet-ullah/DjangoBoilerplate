document.querySelectorAll('.alert').forEach( alert => {
    setTimeout(() => {
        alert.classList.add('transition')
        alert.classList.add('duration-[2000ms]')
        alert.classList.add('bg-transparent')
        alert.classList.add('text-transparent')
        alert.classList.remove('shadow')
        setTimeout(() => {
            alert.remove()
        }, 2000)
    }, 2000)
})

document.querySelectorAll('.form-input').forEach( formInput => {
    let label = formInput.querySelector('label')
    let input = formInput.querySelector('input')

    if(input.value.length > 0) {
        label.classList.remove('-translate-y-6')
        label.classList.add('text-sm')
        label.classList.remove('text-xs')
    }

    input.addEventListener('focus', () => {
        label.classList.add('-translate-y-6')
        label.classList.remove('text-sm')
        label.classList.add('text-xs')
    })
    input.addEventListener('blur', () => {
        if(input.value.length <= 0) {
            label.classList.remove('-translate-y-6')
            label.classList.add('text-sm')
            label.classList.remove('text-xs')
        }
    })
})