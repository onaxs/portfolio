/**
 * Physics Module for 1D Particle Laser Cooling Simulation
 *
 * This module implements the physics for laser cooling including:
 * - Doppler shift calculations
 * - Resonance conditions
 * - Recoil energy and momentum transfer
 * - Position and velocity updates
 */

// Physical constants
const h = 6.626e-34;  // Planck constant (J*s)
const c = 3e8;  // Speed of light (m/s) - also v_m (wave propagation speed in medium)
const v_s = 0;  // Speed of laser source relative to medium (stationary)

// Master scaling factor for cooling visualization
// This single parameter controls how quickly the particle cools down
// Adjust this value to make cooling more visible (higher = faster cooling)
const COOLING_SCALE = 5e10;  // Master scaling factor for visual cooling effect

// Velocity scaling factor for Doppler shift calculations
// This makes the velocity changes more significant in the Doppler shift formula
// Higher values = velocity changes affect resonance more dramatically
const VELOCITY_SCALE = 1e6;  // Scales velocity in Doppler calculations

/**
 * Calculate Doppler shifted frequency
 * Formula: f_s = f_0 * (v_m + v_r) / (v_m + v_s)
 *
 * @param {number} f_0 - Emitter frequency (laser frequency)
 * @param {number} v_particle - Particle velocity
 * @param {boolean} towardLaser - Whether particle is moving toward the laser
 * @returns {number} Doppler shifted frequency
 */
function getDopplerShiftedFrequency(f_0, v_particle, towardLaser) {
    // v_r is positive when particle moves toward the laser source
    // Scale velocity to make Doppler shift more significant
    const v_r = towardLaser ? v_particle * VELOCITY_SCALE : -v_particle * VELOCITY_SCALE;
    const f_s = f_0 * (c + v_r) / (c + v_s);
    return f_s;
}

/**
 * Check if Doppler shifted laser frequency matches transition frequency
 *
 * @param {number} laserFreq - Laser frequency (f_0)
 * @param {number} v_particle - Particle velocity
 * @param {number} transitionFreq - Transition frequency (f_t)
 * @param {boolean} towardLaser - Whether particle is moving toward the laser
 * @param {number} tolerancePercent - Resonance tolerance as percentage (default 0.5%)
 * @returns {boolean} True if resonance condition is satisfied
 */
function isResonant(laserFreq, v_particle, transitionFreq, towardLaser, tolerancePercent = 0.5) {
    const f_s = getDopplerShiftedFrequency(laserFreq, v_particle, towardLaser);
    const f_t = transitionFreq;

    // Calculate tolerance margin: if |f_s - f_t| < margin, cooling occurs
    const tolerance = f_t * (tolerancePercent / 100);
    return Math.abs(f_s - f_t) < tolerance;
}

/**
 * Calculate new velocity after photon absorption and emission
 *
 * @param {number} vx - Current particle velocity
 * @param {number} m - Particle mass
 * @returns {number} New velocity after energy loss
 */
function calculateVelocityAfterCooling(vx, m) {
    // Calculate recoil frequency: w_r = h * v^2 / (2 * m)
    const w_r = (h * vx * vx) / (2 * m);

    // Recoil energy: E_R = h * w_r
    const E_R = h * w_r;

    // Energy loss reduces velocity (E = 0.5 * m * v^2)
    // E_new = E_old - E_R
    // 0.5 * m * v_new^2 = 0.5 * m * v_old^2 - E_R
    const E_kinetic = 0.5 * m * vx * vx;

    // Apply COOLING_SCALE to make the effect visible
    const E_new = Math.max(0, E_kinetic - E_R * COOLING_SCALE);
    const v_new = Math.sqrt(2 * E_new / m);

    return v_new;
}

/**
 * Update particle physics including position, boundary collisions, and laser cooling
 *
 * @param {Object} state - Current simulation state
 * @param {number} state.x - Particle position
 * @param {number} state.vx - Particle velocity
 * @param {Object} params - Simulation parameters
 * @param {number} params.m - Particle mass
 * @param {number} params.boundaryRadius - Boundary radius
 * @param {number} params.transitionFreq - Transition frequency
 * @param {boolean} params.leftLaserOn - Left laser enabled
 * @param {boolean} params.rightLaserOn - Right laser enabled
 * @param {number} params.leftLaserFreq - Left laser frequency
 * @param {number} params.rightLaserFreq - Right laser frequency
 * @param {number} params.resonanceTolerance - Resonance tolerance percentage (default 0.5%)
 * @param {number} dt - Time step
 * @returns {Object} Updated state {x, vx}
 */
function updatePhysics(state, params, dt) {
    let { x, vx } = state;
    const {
        m,
        boundaryRadius,
        transitionFreq,
        leftLaserOn,
        rightLaserOn,
        leftLaserFreq,
        rightLaserFreq,
        resonanceTolerance = 0.5
    } = params;

    // Update position
    x += vx * dt;

    // Enforce boundary with elastic collision
    if (Math.abs(x) > boundaryRadius) {
        x = Math.sign(x) * boundaryRadius;
        vx = -vx;
    }

    // Laser interaction
    // Only the laser opposite the direction of current motion can affect the particle

    if (vx > 0 && rightLaserOn) {
        // Right laser (from right, traveling left) acts when particle moves right (toward it)
        if (isResonant(rightLaserFreq, Math.abs(vx), transitionFreq, true, resonanceTolerance)) {
            const v_new = calculateVelocityAfterCooling(vx, m);
            vx = vx > 0 ? v_new : -v_new;  // Maintain direction
            if (Math.abs(vx) < 0.1) vx = 0;
        }
    } else if (vx < 0 && leftLaserOn) {
        // Left laser (from left, traveling right) acts when particle moves left (toward it)
        if (isResonant(leftLaserFreq, Math.abs(vx), transitionFreq, true, resonanceTolerance)) {
            const v_new = calculateVelocityAfterCooling(vx, m);
            vx = vx > 0 ? v_new : -v_new;  // Maintain direction
            if (Math.abs(vx) < 0.1) vx = 0;
        }
    }

    return { x, vx };
}

// Export functions for use in main HTML file
// (Using global scope for browser compatibility without module bundler)
window.PhysicsEngine = {
    getDopplerShiftedFrequency,
    isResonant,
    calculateVelocityAfterCooling,
    updatePhysics,
    constants: { h, c, v_s, COOLING_SCALE, VELOCITY_SCALE }
};
