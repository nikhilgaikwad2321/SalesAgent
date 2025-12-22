package com.crm.ai.service;

import com.crm.ai.client.LlmRuntimeClient;
import com.crm.ai.dto.AiRequestDto;
import com.crm.ai.dto.AiResponseDto;
import com.crm.ai.dto.LlmRequestDto;
import com.crm.ai.dto.LlmResponseDto;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class AiAssistService {

    private final LlmRuntimeClient llmRuntimeClient;

    public AiResponseDto getAssistance(AiRequestDto request) {
        log.info("Received AI assistance request: {}", request);

        // 1. Validation (Basic example)
        if (request.getQuery() == null || request.getQuery().trim().isEmpty()) {
            throw new IllegalArgumentException("Query cannot be empty");
        }

        // 2. Map to LLM Request
        LlmRequestDto llmRequest = LlmRequestDto.builder()
                .intent(request.getIntent())
                .query(request.getQuery())
                .filters(request.getFilters())
                .build();

        // 3. Call LLM Runtime
        try {
            LlmResponseDto llmResponse = llmRuntimeClient.generateResponse(llmRequest);
            
            // 4. Map back to Response
            // Assuming confidence is high if successful for now, as LLM runtime doesn't return confidence score yet
            return new AiResponseDto(llmResponse.getResponse(), "HIGH");
        } catch (Exception e) {
            log.error("Error calling LLM Runtime", e);
            throw new RuntimeException("Failed to get response from AI service");
        }
    }
}
