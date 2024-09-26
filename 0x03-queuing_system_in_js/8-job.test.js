/*eslint-disable*/
import { expect } from 'chai';
import { describe, it, beforeEach, afterEach } from 'mocha';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

// const queue = kue.createQueue();
describe('createPushNotificationsJobs', function() {
    let queue;
    
    beforeEach(() => {
        // Initialize the queue in test mode
        queue = kue.createQueue();
        queue.testMode.enter();
    });
    afterEach(() => {
        // Exit test mode and clear the queue
        queue.testMode.clear();
        queue.testMode.exit();
    });
    it('should throw an error if jobs is not an array, passing string', function() {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
            'Jobs is not an array'
        );
    });
    it('should throw an error if jobs is not an array, passing number', function() {
        // const jobs = [
        //     {
        //         phoneNumber: '4153518780',
        //         message: 'This is the code 1234 to verify your account',
        //     },
        //     {
        //         phoneNumber: '4153518781',
        //         message: 'This is the code 4562 to verify your account',
        //     },
        // ];
        expect(() => createPushNotificationsJobs(2, queue)).to.throw(
            'Jobs is not an array'
        );

        // // Check the first job's data
        // expect(queue.testMode.jobs[0].data).to.eql({
        //     phoneNumber: '4153518780',
        //     message: 'This is the code 1234 to verify your account',
        // });

        // // Check the second job's data
        // expect(queue.testMode.jobs[1].data).to.eql({
        //     phoneNumber: '4153518781',
        //     message: 'This is the code 4562 to verify your account',
        // });
    });
    it('should throw an error if jobs is not an array, passing object', function() {
        // const jobs= [
        //     {
        //         phoneNumber: '415318780',
        //         nessage: 'This is the code 1234 to verify your account',
        //     },
        // ];
        // const consoleSpy = sinon.spy(console, 'log');
        // createPushNotificationsJobs(jobs, queue);

        // expect(consoleSpy.calledWithMatch(/Notification job created:/)).to.be.true;
        // consoleSpy.restore();
        expect(() => createPushNotificationsJobs({}, queue)).to.throw(
            'Jobs is not an array'
        );
    });
    it('should NOT display a error message if jobs is an array with empty array', function() {
    const jobs = [];
    const ping = createPushNotificationsJobs(jobs, queue);
    // const job = queue.testMode.jobs[0];

    // // SImulate job progress
    // job.progress(50);

    // // No real processing done, but one can check if the progress is tracked
    expect(ping).to.equal(undefined);
    });
});
