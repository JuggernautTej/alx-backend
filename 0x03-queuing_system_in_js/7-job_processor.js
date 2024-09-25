/*eslint-disable*/
import kue from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
    // Track the job's progress from 0-100 %
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    // Simulate progress from 50%
    job.progress(50, 100);
    console.log(`Sending notfiication to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});