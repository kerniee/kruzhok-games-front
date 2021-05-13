const values = [2, 2, 3, 5, 7, 8, 8, 10, 11, 11, 9, 8, 7, 5, 4]

const labels = values.map((value) => {
    return value.toString() + "%"
});

const colors = values.map((value, index, array) => {
    if (index === 11) {
        return '#0C7D84'
    } else return 'rgba(12,125,132,0.5)'
})
const data = {
    labels: labels,
    datasets: [{
        label: 'Рейтинг',
        backgroundColor: colors,
        borderColor: '#0C7D84',
        data: values,
    }],
    borderWidth: 1
};
const config = {
    type: 'bar',
    data,
    options: {
        aspectRatio: 5,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

let myChart = new Chart(
    document.getElementById('myChart'),
    config
);