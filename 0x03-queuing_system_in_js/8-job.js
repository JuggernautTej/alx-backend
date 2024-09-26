/*eslint-disable*/
import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
    // checking if jobs is not an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
            if (!err) {
                if (!queue.testMode) {
                console.log(`Notification job created: ${job.id}`);
            } else {
                console.log('Notification job created (test mode)');
            }
        }
        });
    
        // Handle job completion
        job.on('complete', () => {
            if (!queue.testMode) {
            console.log(`Notification job ${job.id} completed`);
            }
        });
        // Handle job failure
        job.on('failed', (err) => {
            if (!queue.testMode) {
            console.log(`Notification job ${job.id} failed: ${err}`);
            }
        });
        // Handle job progress
        job.on('progress', (progress) => {
            if (!queue.testMode) {
            console.log(`Notification job ${job.id} ${progress}% complete`);
            }
        });
    }
    )};

module.exports = createPushNotificationsJobs;