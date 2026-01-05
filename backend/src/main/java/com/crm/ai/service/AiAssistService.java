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

        // 1. Validation
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
            
            // 4. Intent-based response mapping
            if ("PPT_GENERATION".equals(request.getIntent())) {
                // PPT Generation Response
                AiResponseDto response = new AiResponseDto();
                response.setAnswer(llmResponse.getResponse());
                response.setConfidence("HIGH");
                response.setPptFilePath(llmResponse.getPptFilePath());
                response.setPptFileName(llmResponse.getPptFileName());
                response.setStatus(llmResponse.getStatus());
                return response;
            } else {
                // Standard text response
                AiResponseDto response = new AiResponseDto();
                response.setAnswer(llmResponse.getResponse());
                response.setConfidence("HIGH");
                response.setStatus("TEXT_RESPONSE");
                return response;
            }
        } catch (Exception e) {
            log.error("Error calling LLM Runtime", e);
            throw new RuntimeException("Failed to get response from AI service");
        }
    }
}
