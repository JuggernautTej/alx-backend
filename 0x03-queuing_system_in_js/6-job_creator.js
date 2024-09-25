/*eslint-disable*/
import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '070567812245',
    message: 'Cry me a river',
};

const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        } else {
            console.log('Error creating job:', err);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
});

// job.on('complete', () => {
//     console.log('Notification job failed');
// });

job.on('failed', () => {
    console.log('Notification job failed');
});
